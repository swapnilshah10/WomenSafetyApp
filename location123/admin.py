from django.contrib import admin
from .models import *
from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Marker)
admin.site.register(Locations)