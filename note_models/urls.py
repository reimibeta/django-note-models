from django.conf.urls import url
from django.urls import path, include
from note_models import views
from rest_framework import routers

router = routers.DefaultRouter()
""" branch api """
router.register('branch', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
