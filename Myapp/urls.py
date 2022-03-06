from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Image_view,success

urlpatterns = [
        path('image_upload/',views.Image_view),
        path('success/',views.success),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))