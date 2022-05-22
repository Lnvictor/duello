from django.urls import path

from .views import CageViewSet

urlpatterns = [
    path("cage", 
        CageViewSet.as_view({"post": "create", "get": "list"}), 
         name="cage"), 
    path("cage/<int:id>", CageViewSet.as_view({"get":"retrieve", "delete": "destroy", "put": "update"}), name="cage_by_id")
]
