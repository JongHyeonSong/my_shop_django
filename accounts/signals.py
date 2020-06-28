
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

