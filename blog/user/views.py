from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ProfileUpdateForm,\
    UserUpdateForm,CreateBlogForm,UpdateBlogForm
from .models import Profile
from blogging.models import Blog
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings

def sending_blog(req):
    if req.method == "POST":
        email = req.POST.get("email")
        text = req.POST.get("text")

        send_mail("Blog",message=text,recipient_list=[email],from_email=settings.EMAIL_HOST_USER)
        return redirect(req.META.get("HTTP_REFERER"))
    return render(req,"mail.html")

def register(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user = user)
            return redirect("login")

    context = {
        "form":form
    }
    
    return render(request,'user/register.html',context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,**form.cleaned_data)
            if user:
                login(request,user)
                
                if user.first_name and user.last_name:
                    return redirect('profile')
                else:
                    return redirect('udpate_profile')
                    
            else:
                context['error'] = 'User topilmadi'
        else:
            context['error'] = form.errors

    return render(request,'user/login.html',context)

def logout_view(request):
    logout(request)
    return redirect("login")

def profile(request):
    return render(request,'profile/profile.html')

def update_profile(request):
    
    if request.method == "GET":
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)
    
    if request.method == "POST":    
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    
    context = {
        'profile_form':profile_form,
        'user_form':user_form,
    }

    return render(request,'profile/update_profile.html',context)

def create_blog(request):
    
    form = CreateBlogForm()
    
    if request.method == 'POST':
        form = CreateBlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile")
    
    context = {
        'form':form
    }
        
    return render(request,'profile/create_blog.html',context)
        
def my_blogs(request):
    
    blogs = Blog.objects.filter(author__user = request.user)
    
    context = {
        'blogs':blogs
    }
    
    return render(request,'profile/my_blogs.html',context)

def update_blog(request,id):
    
    
    blog = Blog.objects.get(id = id)
    
    if request.method == "GET":
        form = UpdateBlogForm(instance=blog)
    
    if request.method == "POST":
        
        form = UpdateBlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
    
    context = {
        'form':form
    }
    
    return render(request,'profile/update_blog.html',context)

def delete_blog(request,id):
    Blog.objects.get(id = id).delete()
    
    return redirect("my_blogs")
