from django.urls import path
from .views import Birthdays, Login, Register, User_detail

urlpatterns = [
    path('birthdays/', Birthdays.as_view()),
    path('login/', Login.as_view()),
    path('register/', Register.as_view()),
    path('<int:pk>/', User_detail.as_view()),
    
]

