from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("save/", views.save, name="save"),
    path("random/", views.random_entry, name="random")
]
