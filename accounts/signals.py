
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from .models import Customer
from django.contrib.auth.models import Group


from django.db import models
from django.dispatch import receiver

# @receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group) # user = form.save() = instance
        
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )

post_save.connect(customer_profile, sender=User)


# from django.dispatch import reciever
# @reciever(post_save, sender=User)        
# def update_profile(sender, instance, created, **kwargs):
    
#     if created==False:
#         instance.profile.save() #1:1관계이기때문에 profile로 바로넘어올수있음
#         print("Profile updated")
# post_save.connect(update_profile, sender=User) 