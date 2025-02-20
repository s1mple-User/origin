from django.db.models import Manager,Count
from parler.managers import TranslatableManager
class BlogManager(Manager):
    
    def published_blogs(self):
        return self.get_queryset().filter(status = 'published')  
    
    def get_last_blog(self):
        return self.published_blogs().last()

class CategoryManager(TranslatableManager):
    
    def category_with_blog_count(self):
        return self.get_queryset().annotate(blog_count = Count('blog'))