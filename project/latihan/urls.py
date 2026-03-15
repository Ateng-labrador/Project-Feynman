from django.urls import path

from . import views

# persamaan 

urlpatterns = [
    path('', views.index),
    path("post/<slug:slugInput>/", views.detailPost),
    path("category/<slug:categoryInput>/", views.categoryPost),
]
