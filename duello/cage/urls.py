from django.urls import path

from .views import CageViewSet

urlpatterns = [path("cage", CageViewSet.as_view({"post": "create"}), name="cage")]
