from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    # path('<int:pk>/<title>/<text>/', views.PostListView.as_view(), name='post_list'),
]