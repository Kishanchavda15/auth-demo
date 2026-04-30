from django.urls import path

from user_module.views import RegisterUser, LoginUser, PasswordUpdate

urls_pattern=[
    path("register/",RegisterUser.as_view()),
    path("login/",LoginUser.as_view()),
    path("update/<int:pk>/",PasswordUpdate.as_view())
]
