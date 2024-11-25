from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path("", views.combined_view, name="combined_view"),
path("create/", views.create_todolist, name="create"),
path("home/", views.combined_view, name="combined_view"),
path("logout/", views.logout_view, name="logout"),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('item/delete/<int:item_id>/', views.delete_item, name='delete_item'),
path('todolist/delete/<int:todolist_id>/', views.delete_todolist, name='delete_todolist'),
]