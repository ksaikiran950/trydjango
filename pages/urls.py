from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path('',home_view),
    path('', views.post_list, name='post-list'),
    path('create/', views.post_create, name='post-create'),
    path('<int:id>/', views.post_detail, name='post-detail'),
    path('<int:id>/update/', views.post_update, name='post-update'),
    path('<int:id>/delete/', views.post_delete, name='post-delete'),
]
