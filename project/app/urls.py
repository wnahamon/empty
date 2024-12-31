from django.urls import path
from .views import main, delete, create, read, update
urlpatterns = [
    path('home', main, name='main'),
    path('delete/<int:id>', delete, name='delete'),
    path('create', create, name='create'),
    path('product/<int:id>', read, name='read'),
    path('update/<int:id>', update, name='update'),
]