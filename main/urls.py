from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path("", views.combined_view, name="combined_view"),
path("create/", views.create_todolist, name="create"),
path("home/", views.combined_view, name="combined_view"),
path("logout/", views.logout_view, name="logout"),
path('login/', auth_views.LoginView.as_view(), name='login'),
]