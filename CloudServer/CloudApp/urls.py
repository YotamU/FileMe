from django.urls import path
from. import views
urlpatterns = [
    path('',views.LoginPage),
    path("Login", views.LoginPage, name="login"),
    path("Register", views.registerPage,name="register"),
    path("admin", views.Admin, name="admin"),

]