from django.urls import path, include
from .views import UserLoginView, UserLogoutView, user_register_view

urlpatterns = [
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('register/', UserRegisterView.as_view(), name='register'),
    path('register/', user_register_view, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]