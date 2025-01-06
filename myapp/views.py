from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import SignUpForm,SignInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form_instance=SignUpForm()
        return render(request,"signup.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=SignUpForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            User.objects.create_user(**data)
            print("=====Account Created=====")
            return redirect("signin")
        else:
            print("xxxxxxfailedxxxxxxx")
            return render(request,"signup.html",{"form":form_instance})

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form_instance=SignInForm()
        return render(request,"signin.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=SignInForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")
            print(uname,pwd)
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print(request.user)
                print("session started")
            else:
                print("invalid credentials")
            return redirect("signin")



