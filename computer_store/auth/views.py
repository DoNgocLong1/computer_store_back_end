from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class MultiSiteTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # request.data["username"] = f"{request.site.id}::{request.data.get('email')}"
        return super().post(request, *args, **kwargs)
