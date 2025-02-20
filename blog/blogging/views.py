from django.shortcuts import render,redirect
from .forms import CommentForm
from django.http.response import JsonResponse
from history.models import History
from user.models import Profile
from .models import Blog,Comment,Category
from django.db.models import Count
from django.core.paginator import Paginator

def home(request):

    blogs = Blog.objects.published_blogs()
    categories = Category.objects.category_with_blog_count()
    main_blog = Blog.objects.get_last_blog()

    header_blogs = []
    
    temp = []
    
    for blog in blogs:
        temp.append(blog)
        if len(temp) == 4:
            header_blogs.append(temp)
            temp = []
    
    context = {
        'blogs':blogs,
        'categories':categories,
        'header_blogs':header_blogs,
        'main_blog':main_blog,
    }
    
    return render(request,'new/index.html',context)

def blogs(request,category=None):
    blogs = Blog.objects.annotate(comment_count = Count('comment'))
    
    categories = Category.objects.annotate(blog_count = Count('blog'))
    
    if category:
        category = Category.objects.get(id = category)
        blogs = blogs.filter(category = category)

    title = request.GET.get('title',None)
    
    if title:
        blogs = blogs.filter(title__icontains = title)
        
    


    paginator = Paginator(blogs,per_page=10)
    
    page = request.GET.get('page',1)
    
    paginated_blogs = paginator.get_page(page)

    context = {
        "blogs":paginated_blogs,
        "category":category,
        'categories':categories,
    }
    
    return render(request,'new/blogs.html',context)

def about(request):
    return render(request,'new/about.html')

def contact_us(request):
    return render(request,'new/contact.html')

def blog_details(request,id):
    blog = Blog.objects.annotate(comment_count = Count('comment')).get(id = id)
    
    if hasattr(request.user,'profile'):
        History.objects.get_or_create(user = request.user.profile, blog = blog)
    
    seen = request.session.get(f'blog_{blog.id}',None)
    if not seen:
        blog.add_view
        request.session[f"blog_{blog.id}"] = blog.id
    comments = Comment.objects.filter(blog = blog,reply__isnull = True)
    form = CommentForm()
    
    
    other_blogs = Blog.objects.filter(author = blog.author).exclude(id = blog.id)
    
    previous = None
    next = None
    
    if other_blogs.exists():
        if len(other_blogs) >= 2:
            previous = other_blogs.first()
            next = other_blogs.last()
        else:
            next = other_blogs[0]
        
    
    
    context = {
        'blog':blog,
        'form':form,
        'comments':comments,
        'previous':previous,
        'next':next,
    }
    
    return render(request,'new/blog_detail.html',context)

def create_comment(request,blog_id):
    if request.method == "POST":
        
        blog = Blog.objects.get(id = blog_id)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            
            form.instance.blog = blog
            form.instance.user = request.user.profile
            
            form.save()
    
    return redirect(request.META.get("HTTP_REFERER"))

def like_view(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    if hasattr(request.user,'profile'):
        blog.add_like(request.user.profile)        
    return JsonResponse({"like":blog.likes.count(),"dislike":blog.dislike.count()})

def dislike_view(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    if hasattr(request.user,'profile'):
        blog.add_dislike(request.user.profile)                
    return JsonResponse({"like":blog.likes.count(),"dislike":blog.dislike.count()})
    
def subscribe(request,author_id):
    profile = Profile.objects.get(id = author_id)
    if hasattr(request.user,'profile'):
        data = profile.subscribe(request.user.profile)
        data = 'unsubscribe' if data else 'unsubscribe'         
    return JsonResponse({"data":data})
    
    
    


    
    

