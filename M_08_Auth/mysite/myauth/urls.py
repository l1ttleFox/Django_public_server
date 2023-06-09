from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    MyAuthLogoutView,
    set_cookies_view,
    get_cookies_view,
    set_session_view,
    get_session_view,
)


app_name = "myauth"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='myauth/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', MyAuthLogoutView.as_view(), name="logout"),
    path("cookies/set/", set_cookies_view, name="set_cookies"),
    path("cookies/get/", get_cookies_view, name="get_cookies"),
    path("sessions/set/", set_session_view, name="set_sessions"),
    path("sessions/get/", get_session_view, name="get_sessions"),
]