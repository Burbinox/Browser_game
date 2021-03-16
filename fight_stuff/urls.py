from django.urls import path
from . import views

urlpatterns = [
    path('user_stats/', views.show_user_stats),
]
