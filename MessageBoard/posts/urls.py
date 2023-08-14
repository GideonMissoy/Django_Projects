from django.urls import path
from .views import HopePageView

urlpatters = [
    path("", HomePageView.as_view(), name='home'),
]