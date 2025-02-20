from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogging.models import Blog
from .models import Profile


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','status','description','image']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age','bio','image','phone']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class CreateBlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['author','title','status','description','image']