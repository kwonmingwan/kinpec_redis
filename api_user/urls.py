from api_user import views
from django.urls import path, include

urlpatterns = [
    path('v1/api/user/', views.UserListAction.as_view()),
]