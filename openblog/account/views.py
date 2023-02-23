from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,FormView
from .forms import RegForm,LogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
#class HomeView(View):
#    def get(self,request,*args,**kwargs):
#        return render(request,"main_home.html")

class HomeView(TemplateView):
    template_name="main_home.html"


#class RegView(View):
#    def get(self,request,*args,**kwargs):
#        f=RegForm()
#        return render(request,"reg.html",{"form":f})
#    def post(self,request,*args,**kwargs):
#        form_data=RegForm(data=request.POST)    
#        if form_data.is_valid():
#            form_data.save()
#            messages.success(request,"User Registered Successsfully!!!")
#            return redirect("h")
#        else:
#            messages.error(request,"User Registered failed!!!")
#            return render(request,"reg.html",{"form":form_data}) 


class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')


#class RegView(View):
#    template_name="reg.html"
#    form_class=RegForm
#    model=User
#    def get(self,request,*args,**kwargs):
#      f=RegForm()
#      return render(request,"reg.html",{"form":f})
#    def post(self,request,*args,**kwargs):
#        form_data=RegForm(data=request.POST)    
#        if form_data.is_valid():
#            form_data.save()
#            messages.success(request,"User Registered Successsfully!!!")
#            return redirect("h")
#        else:
#            messages.error(request,"User Registered failed!!!")
#            return render(request,self.template_name,{"form":form_data}) 


#class LogView(View):
#    def get(self,request):
#        f=LogForm()
#        return render(request,"log.html",{"form":f})
#    def post(self,request,*args,**kwargs):
#        form_data=LogForm(data=request.POST)   
#        if form_data.is_valid():
#            un=form_data.cleaned_data.get("username") 
#            pw=form_data.cleaned_data.get("password") 
#            user=authenticate(request,username=un,password=pw)
#            if user:
#                return redirect("uhome")
#            else:
#                return redirect("log")
#        else:
#            return render(request,"log.html",{"form":form_data})

class LogView(FormView):
    form_class=LogForm
    template_name="log.html"
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)   
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username") 
            pw=form_data.cleaned_data.get("password") 
            user=authenticate(request,username=un,password=pw)
            if user:
                login(request,user)
                return redirect("uhome")
            else:
                return redirect("log")
        else:
            return render(request,"log.html",{"form":form_data})

class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect("log")