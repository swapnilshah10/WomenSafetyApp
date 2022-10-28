from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Voice(models.Model):
    sounds = models.FileField(null=True , upload_to="voice/") 
    user_id = models.ForeignKey(User ,null = True , blank = True, on_delete=models.CASCADE)