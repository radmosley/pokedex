from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterationView, LogoutView, UserObtainTokenPairView

app_name = 'users'

urlpatterns = [
    # path('register', RegisterationView.as_view(), name='register'),
    # path('login', UserObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('logout', LogoutView.as_view(), name='token_obtain_pair'),
]