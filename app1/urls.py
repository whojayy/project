from django.urls import path
from .views import datapost, proadd, productdelete, searchview, index, aboutus, signupview, login, contactus, proall, productview

urlpatterns = [
    path('',index, name='index'),
    path('signupview/',signupview, name='signup'),
    path('login/',login, name='login'),
    path('contactus/',contactus, name='contactus'),
    path('aboutus/',aboutus, name='aboutus'),
    # path('index/',index, name='home'),
    path('datapost/',datapost, name='datapost'),
    path('view/<int:abc>',productview, name='proview'),
    path('delete/<int:abc>',productdelete, name='prodel'),
    path('proall/',proall, name='proall'),
    path('search/',searchview, name='search'),
    path('proadd/',proadd, name='proadd')
]
