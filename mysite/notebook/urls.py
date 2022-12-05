from django.urls import path

from . import views
from .views import delete_document, register_request

# app_name = "notebook"

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

]
