from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/register/', views.RegisterUserView.as_view(), name='register'),
    path('api/v1/login/', views.LoginUserView.as_view(), name='login'),
    path('api/v1/confirm/', views.ConfirmUserView.as_view(), name='confirm'),
]
