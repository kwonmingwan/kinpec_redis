from api_user import views
from django.urls import path, include

urlpatterns = [
    path('/v1/api/user/list', views.UserListAction.as_view()),
    path('/v1/api/user/post', views.UserRegisterAction.as_view()),
]