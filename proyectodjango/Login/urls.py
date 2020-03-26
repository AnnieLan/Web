from django.contrib.auth import views as auth_view
from Login.views import LandingClass
from Login.views import LoginClass
from Login.views import DashboardClass
from django.urls import include, path, re_path

app_name = 'Login'

urlpatterns = [
    path('', LandingClass.as_view(), name='Landing'),
    path('Login/', LoginClass.as_view(), name='Login'),
    path('Dashboard', DashboardClass.as_view(), name='dashboard')
]