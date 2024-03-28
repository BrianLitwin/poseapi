from django.urls import path
from . import views

urlpatterns = [
    path('img_keypoints', views.img_keypoints, name='img_keypoints'),
]