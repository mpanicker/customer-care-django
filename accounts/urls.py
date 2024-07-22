from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:account_id>/", views.getAccount, name="getAccount"),
    path("<int:account_id>/device/", views.getAccountDevices, name="getAccountDevices"),
]