from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('upload/', views.upload_material, name='upload_material'),

    path('<int:pk>/', views.material_detail, name='material_detail'),

    path('<int:pk>/edit/', views.edit_material, name='edit_material'),
    path('<int:pk>/delete/', views.delete_material, name='delete_material'),

    path('<int:pk>/bookmark/', views.add_bookmark, name='add_bookmark'),
    path(
        '<int:pk>/remove-bookmark/',
        views.remove_bookmark,
        name='remove_bookmark'
    ),

    path(
        '<int:pk>/review/',
        views.add_review,
        name='add_review'
    ),
    path(
        'review/<int:pk>/delete/',
        views.delete_review,
        name='delete_review'
    ),
]