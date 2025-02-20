from django.dispatch import receiver,Signal
from django.db.models.signals import pre_save,post_save
from .models import Blog
from django.core.mail import send_mail
from django.conf import settings

new_signle =Signal()
@receiver(new_signle)
def listen_new_signal(sender,**kwargs):
    print(kwargs.get(sender,"mydata"))

@receiver(new_signle)
def pre_save_blog(sender,instance,**kwargs):
    instance.status = Blog.StatusEnum.DRAFT

@receiver(post_save,sender = Blog)
def pre_save_blog(sender,instance,created,**kwargs):
    if created:
        print("Send Email")
        send_mail("Blog",message="Text",recipient_list=["u3905173@gmail.com"],from_email=settings.EMAIL_HOST_USER)
    else:
        print(instance,"Send Email")
