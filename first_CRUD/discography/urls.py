from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='discography'),
    path('disc/create', views.create_disc, name='disc-create'),
    path('disc/edit/<int:id>/', views.edit_disc, name='disc-edit'),
    path('disc/delete/<int:id>/', views.delete_disc, name='disc-delete'),
]
