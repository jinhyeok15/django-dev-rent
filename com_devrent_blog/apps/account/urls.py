from django.urls import path
from . import views
from .apps import AccountConfig

app_name = AccountConfig.name


urlpatterns = [
    # path('logout/'),
    path('login/', views.login, name='login'),
    # path('signup/'),
    # path('delete/')
]
