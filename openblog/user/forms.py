from django import forms
from account.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']
        

class CPassForm(forms.Form):
    old_pass=forms.CharField(max_length=100,label="Old Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Old Password"}))
    new_pass=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter New Password"}))
    confirm_pass=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-Enter New Password"}))