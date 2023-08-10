from django.urls import path
from department import views

app_name = "department"

urlpatterns = [
    path("", views.ListCreateDepartamentoView.as_view(), name=""),
    path("<int:pk>", views.DetailApiView.as_view(), name=""),
]