from django.urls import path
from . import views


urlpatterns = [
    path('upload-profile-image/', views.upload_profile_image, name='upload_profile_image'),
]