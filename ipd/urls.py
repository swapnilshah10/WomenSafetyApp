from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('location/' , include('location123.urls')),
    path('file/' , include('sound.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
