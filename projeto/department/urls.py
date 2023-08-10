from django.urls import path
from department import views

app_name = "department"

urlpatterns = [
    path("criar", views.CreateDepartamentoView.as_view(), name="criar"), 
    path("", views.ListarDepartamentoView.as_view(), name=""),
    path("<int:id>", views.ListarOneDepartamentoView.as_view(), name=""),
    path("editar/<int:id>", views.EditDepartamentoView.as_view(), name="editar"),
    path("delete/<int:id>", views.DeleteDepartamentoView.as_view(), name="delete")
]