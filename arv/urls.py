from django.urls import path
from . import views

urlpatterns = [
    path('arvs/', views.arv_list, name='arv_list'),
    path('arvs/<int:pk>/', views.arv_detail, name='arv_detail'),
]
