from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'subscribe', views.SubscriptionViewset, basename='subscribe')

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
] + router.urls
