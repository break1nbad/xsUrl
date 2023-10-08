from django.urls import path
from home import views

urlpatterns = [
    path("<str:base62_id>", views.follow, name='follow'),
]
