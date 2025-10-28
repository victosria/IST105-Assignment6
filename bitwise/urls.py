from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_view, name='input_home'),
    path('entries/', views.list_entries_view, name='list_entries'),
]
