from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path("post/<slug:slugInput>/", views.detailPost),
    path("post/<slug:categoryInput>/", views.categoryPost),
]

