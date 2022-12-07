from django.urls import path

from . import views
from .views import delete_document

# app_name = "notebook"

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    # path('my_notes/new', views.UserNoteCreateView.as_view(), name='my-new-note'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('search/', views.search, name='search'),

]
