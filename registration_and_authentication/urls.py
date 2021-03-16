from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout),
    path('show_all_object_from_db', views.show_all_object_from_db)
]
