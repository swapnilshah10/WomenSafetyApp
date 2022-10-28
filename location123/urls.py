from django.urls import path
from . import views as view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as v

urlpatterns = [
    path ('getmarkers/' , view.getmarkers),
    path('postmarker/' , view.postmarker),
    path('postlocation/' , view.postlocation),
    path('api-auth/', v.obtain_auth_token),
    path('get-details/',view.UserDetailAPI.as_view()),
    path('register/',view.RegisterUserAPIView.as_view()),
    path('login/', view.login)
]