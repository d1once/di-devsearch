from django.urls import path
from . import views

urlpatterns = [
    path('', views.kot_view, name='kot'),
    path('create-kot/', views.create_kot, name="create-kot"),
    path('update-kot/<str:pk>', views.update_kot, name="update-kot")
]
