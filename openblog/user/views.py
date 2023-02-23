from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import ProfileForm,CPassForm
from account.models import UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate,logout
# Create your views here.

#class UserHome(View):
#    def get(self,request):
#        return render(request,"userhome.html")


class UserHome(TemplateView):
    template_name="userhome.html"

class ProfileView(TemplateView):
    template_name="profile.html"    

class AddProfile(CreateView):
    template_name="addprofile.html"
    form_class=ProfileForm
    model=UserProfile
    success_url=reverse_lazy("profile")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Profile Added!!")
        return super().form_valid(form)
    #def post(self,request,*args,**kwargs):
    #    form_data=self.form_class(data=request.POST,files=request.FILES)
    #    if form_data.is_valid():
    #        form_data.instance.user=request.user
    #        form_data.save()
    #        return redirect("profile")
    #    else:
    #        return render(request,"addprofile.html",{"form":form_data})


class CPassView(FormView):
    template_name="cpass.html"
    form_class=CPassForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            old=form.cleaned_data.get("old_pass")
            new=form.cleaned_data.get("new_pass")
            cnf=form.cleaned_data.get("confirm_pass")
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==cnf:
                    #user.password=new
                    #user.save()
                    user.set_password(new)#to change password in a user object
                    user.save()
                    logout(request)
                    messages.success(request,"Password Changed!")
                    return redirect("log")
                else:
                    messages.error(request,"Password mismatch")
                    return redirect("cpassword")
            else:
                messages.error(request,"Old password entered is incorrect!!")
                return redirect("cpassword")            
