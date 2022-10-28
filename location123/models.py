from django.db import models
from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    @property
    def token(self):
        token = Token.objects.get(user=User.objects.get(self.id))
        return token

class Marker(models.Model):
    name = models.CharField(max_length=30 , null=True)
    latitude = models.FloatField(null = False)
    longitude = models.FloatField(null = False)
    isSafe = models.BooleanField(null = False , default=True)
    user_id = models.ForeignKey(User ,null = True , blank = True, on_delete=models.CASCADE)
    def __str__(self):
        r = str(self.id ) + "," + str(self.latitude) + "," + str(self.longitude)+" ,Safe: "+str(self.isSafe)
        return r

    def create_marker(name , latitude , longitude , isSafe ,user_id):
        marker = Marker(name = name , latitude = latitude , longitude = longitude , isSafe = isSafe ,user_id = user_id)
        marker.save()
        return marker
    
    def get_all_markers(user_id):
        queryset = Marker.objects.filter(user_id=user_id)
        return queryset
    
    def delete_marker(id):
        Marker.get(id=id).delete()
        return True

class Locations(models.Model):
    latitude = models.FloatField(null = False)
    longitude = models.FloatField(null = False)
    isSafe = models.BooleanField(null = True , blank = True, default=True)
    def __str__(self):
        r = str(self.id ) + "," + str(self.latitude) + "," + str(self.longitude)+" ,Safe: "+str(self.isSafe)
        return r

    def create_marker(name , latitude , longitude , isSafe):
        marker = Locations(name = name , latitude = latitude , longitude = longitude , isSafe = isSafe)
        marker.save()
        return marker
    
    def get_all_markers():
        queryset = Locations.objects.all()
        return queryset
    
    def delete_marker(id):
        Locations.get(id=id).delete()
        return True