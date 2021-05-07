from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('encrypt_data/<int:pk>/', views.Encrypt),
    path('decrypt_data/<str:encryptkey>/', views.Decrypt, name='encrypt_url'),
    path('sync/', views.Main, name='sync_view'),
    path('async/', views.AsyncMain, name='async_view'),
    path('excel/', views.Excel),
    path('audio/', views.FileView, name='file-upload'),
    path('twilio_call/', views.twiliocall),
    path('twilio_msg/', views.twiliomsg),
    # path('encrypt/', views.encrypt),
    # path('decrypt/', views.decrypt),
]
