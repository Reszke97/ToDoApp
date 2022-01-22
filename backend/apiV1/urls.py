from django.urls import path
# from rest_framework import views
from .views import *


urlpatterns = [
    # User
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/v1/token/refresh/', CustomTokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/v1/token/verify/', CustomTokenVerifyView.as_view(), name = 'token_verify'),
    path('api/v1/user/register/', CustomUserCreate.as_view(), name = "register"),
    path('api/v1/user/logout/', BlacklistTokenUpdateView.as_view(), name = 'logout'),
    path('api/v1/addtodo/', AddToDo.as_view(), name = 'logout'),
    path('api/v1/gettodo/', GetTask.as_view(), name = 'get_task'),
]