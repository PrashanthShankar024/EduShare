from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('profile/', views.profile, name='profile'),
]