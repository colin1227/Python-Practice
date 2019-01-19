from django.urls import path
from .views import Birthdays, Accounts

urlpatterns = [
    # path('', views.people_list, name='people_list'),
    # path('people/<int:pk>', views.people_detail, name="people_show"),
    # path('people/new', views.people_create, name='people_new'),
    path('birthdays/', Birthdays.as_view()),
    path('login/', Accounts.as_view()),
]
