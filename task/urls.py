from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('create', views.create),
    path('read/<int:id>', views.get_one),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
