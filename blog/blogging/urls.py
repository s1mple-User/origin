from django.urls import path
from .views import home,blog_details,create_comment,like_view,dislike_view,blogs,subscribe,\
    about,contact_us

from django.views.generic import RedirectView
urlpatterns = [
    path("/en/",RedirectView.as_view(),name='home'),
    path("home/",home,name='home'),
    path("blog_details/<int:id>/",blog_details,name='blog_details'),
    path("create-comment/<int:blog_id>/",create_comment,name='create_comment'),
    path("like/<int:blog_id>/",like_view,name='like'),
    path("dislike/<int:blog_id>/",dislike_view,name='dislike'),
    path("blogs/<int:category>/",blogs,name="blogs"),
    path("blogs/",blogs,name="blogs-filter"),
    path("subscribe/<int:author_id>/",subscribe,name="subscribe"),
    path("about/",about,name="about"),
    path("contact_us/",contact_us,name="contact_us"),
]