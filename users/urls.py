from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("login/github/", views.github_login, name="github-login"),
    path("login/github/callback/", views.github_callback, name="github-callback"),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("sigup/", views.Signup.as_view(), name="signup"),
    path(
        "verify/<str:key>/", views.complete_verification, name="complete-verification"
    ),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile")
]