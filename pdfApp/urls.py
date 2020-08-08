from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_upload, name="file_upload"),
    path('download/', views.file_download, name='file_download')
]