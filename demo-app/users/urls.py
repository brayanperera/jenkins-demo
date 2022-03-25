from django.conf.urls import include
from users.views import dashboard
from django.urls import path


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("dashboard/", dashboard, name="dashboard"),
]