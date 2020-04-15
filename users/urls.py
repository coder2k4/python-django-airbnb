from django.urls import path

from users.views import Logout, Login, Sighup, complete_verification

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('sighup/', Sighup.as_view(), name='sighup'),
    path('verification/<str:key>', complete_verification, name='sighup'),
]