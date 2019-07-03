from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("update", views.update, name="update"),
    path("library", views.library, name="library"),
    path("playlist/<slug>", views.playlist, name="playlist"),
    path("playlist/<slug>/add", views.add_playlist, name="add_playlist"),
    path("playlist/<slug>/edit", views.edit_playlist, name="edit_playlist"),
    path("playlist/<slug>/delete", views.delete_playlist, name="delete_playlist"),
    path("playlist/<slug>/remove", views.remove_playlist, name="remove_playlist"),
    path("channel/<slug>", views.channel, name="channel"),
    path("channel/<slug>/edit", views.edit_channel, name="edit_channel"),
    path("channel/<slug>/update", views.update_channel, name="update_channel"),
    path("channel/<slug>/delete", views.delete_channel, name="delete_channel"),
    path("create/playlist", views.create_playlist, name="create_playlist"),
    path("create/channel", views.create_channel, name="create_channel"),
    path("pattern/delete", views.delete_filter, name="delete_filter"),
    path("pattern/create", views.create_filter, name="create_filter"),
    path("api/find-channel", views.api_find_channel, name="api_find_channel")
]
