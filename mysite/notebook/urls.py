from django.urls import path

from . import views
from .views import delete_document

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),

]
