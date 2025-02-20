from django.urls import path
from .views import register,login_view,logout_view,\
    profile,update_profile,create_blog,my_blogs,update_blog,delete_blog,sending_blog

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    
    path('profile/',profile,name='profile'),
    path('create_blog/',create_blog,name='create_blog'),
    path('update_profile/',update_profile,name='udpate_profile'),
    path('update_blog/<int:id>/',update_blog,name='update_blog'),
    path('my_blogs/',my_blogs,name='my_blogs'),
    path('sending_blog/',sending_blog,name='sending_blog'),
    path('delete_blog/<int:id>/',delete_blog,name='delete_blog'),
    
]

