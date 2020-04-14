from django.urls import path
from rooms import views as rooms_views

###
# todo:
#  Создать роут для детальной информации комнаты
#  Применить name, namespace, redirect и reserve
#  Применить классы ModelView, ModelDetail
###
from rooms.views import RoomView, RoomDetail, SearchView

app_name = 'rooms'  # для неймспейса
urlpatterns = [
    path("", RoomView.as_view(), name="room_list"),
    path("<int:pk>/", RoomDetail.as_view(), name="room_detail"),
    path("search/", SearchView.as_view(), name="room_search"),
]
