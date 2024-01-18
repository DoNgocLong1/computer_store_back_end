from django.urls import path

from computer_store.auth.views import MultiSiteTokenObtainPairView

urlpatterns = [
    path("token", MultiSiteTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path('token-refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
