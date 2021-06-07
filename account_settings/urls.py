from django.urls import path
from . import views

app_name = "account_settings"

urlpatterns = [
    path('account', views.account, name='account'),
    path('saving_account', views.saving_account, name='saving_account'),
    path('change_password', views.change_password, name='change_password'),
]