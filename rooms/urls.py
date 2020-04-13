from django.urls import path
from rooms import views as rooms_views

###
# todo:
#  Создать роут для детальной информации комнаты
#  Применить name, namespace, redirect и reserve
#  Применить классы ModelView, ModelDetail
###
from rooms.views import RoomView, RoomDetail, room_search

app_name = 'rooms'  # для неймспейса
urlpatterns = [
    path("", RoomView.as_view(), name="room_list"),
    path("<int:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("search/", room_search, name="room_search"),
]
