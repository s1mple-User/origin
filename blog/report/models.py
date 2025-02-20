from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    facebook = models.URLField()
    telegram = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()

    def __str__(self):
        return self.email

class Report(models.Model):
    
    class StatusEnum(models.TextChoices):
        NEW = 'new'
        SEEN = 'seen'
    
    user = models.ForeignKey('user.Profile',on_delete=models.SET_NULL,null=True)
    blog = models.ForeignKey("blogging.Blog",on_delete=models.CASCADE)
    status = models.CharField(max_length=5,choices=StatusEnum.choices,default=StatusEnum.NEW)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)