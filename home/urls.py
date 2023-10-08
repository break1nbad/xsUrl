from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("info/<str:base62_id>", views.info, name='info'),
    path("submit/", views.submit, name='submit'),
    # path("<str:base62_id>", views.follow, name='follow'),
]
