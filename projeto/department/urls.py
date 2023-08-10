from django.urls import path
from department import views

app_name = "department"

urlpatterns = [
    path("", views.ListCreateAPIView.as_view(), name=""),
    path("<int:id>", views.DetailApiView.as_view(), name=""),
]