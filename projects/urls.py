from django.urls import path
from . import views

urlpatterns = [
    path('', views.kot_view, name='kot')
]
