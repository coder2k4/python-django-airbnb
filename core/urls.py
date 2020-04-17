from django.urls import path

from core import views as core_views
from rooms import views as room_views

app_name = 'core'

urlpatterns = [
    path("", room_views.RoomView.as_view(), name="home")
]