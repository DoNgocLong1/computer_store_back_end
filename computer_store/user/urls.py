from django.urls import include, path

from . import views

urlpatterns = [path("get-all-user", views.GetAllUser.as_view(), name="get-all-users")]
