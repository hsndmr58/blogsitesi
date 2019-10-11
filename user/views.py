from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser2 = User(username =  username)
        newUser2.set_password(password)
        newUser2.save()
        login(request,newUser2)
        messages.info(request,"Başarıyla Kayıt oldunuz")

        return redirect("index")
    context ={
            "form":form
        }
    return render(request,"register.html",context)

    
def loginUser(request):
    form = LoginForm(request.POST or None)
    context ={
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)

        print(user)

        messages.info(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.info(request,"başarıyla çıkış yaptınız")
    return redirect("index")
