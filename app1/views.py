from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Pro, Signup
from django.db.models import Q

# Create your views here.

# def hello(request):
#     return HttpResponse("Welcome to the website")

#def signup(request):
    #return render(request,'pages/signup.html')

#def login(request):
    #return render(request,'pages/login.html')

def contactus(request):
    return render(request,'pages/contactus.html')

def aboutus(request):
    return render(request,'pages/aboutus.html')

def index(request):
    return render(request,'pages/index.html')

def datapost(request):
    if request.method=='POST':
        model=Product()
        model.name=request.POST['username']
        model.email=request.POST['email']
        model.save()
    return render(request,'datapost.html')

def productview(request, abc):
    v=Pro.objects.get(id=abc)
    return render(request, 'productview.html',{'v':v})

def productdelete(request, abc):
    v=Pro.objects.get(id=abc)
    v.delete()
    return redirect('proall')

def proall(request):
    l=Pro.objects.all()
    return render(request, 'proall.html',{'l':l})

def signupview(request):
    if request.method=='POST':
        model=Signup()
        model.name=request.POST['name']
        model.email=request.POST['email']
        model.mobile_no=request.POST['mob_no']
        model.password=request.POST['pass']
        model.save()
        
        return redirect('login')

    return render(request,'pages/signup.html')

def login(request):
    if request.method=='POST':
        try:

            m=Signup.objects.get(email=request.POST['email'])
            print(m)
            if m.password==request.POST['pass']:
                print("Pass")
                return redirect('proall')
            else:
                return HttpResponse("Wrong Password")
        except:
            return HttpResponse("Wrong email")

    return render(request,'pages/login.html')

def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('login')
    else:
        return redirect('login')

def searchview(request):
    q=request.GET.get('search')
    if q:
        pr=Pro.objects.filter(Q(name__icontains=q) | Q(des__icontains=q) | Q(price__icontains=q))
        data={'p': pr}
    else:
        data={}

    return render (request, 'pages/search.html', data)

def proadd(request):
    if request.method=='POST':
        model=Pro()
        model.name=request.POST['proname']
        model.price=request.POST['proprice']
        model.des=request.POST['prodes']
        model.img=request.FILES.get('proimg')
        model.save()

    return render(request, 'pages/proadd.html')