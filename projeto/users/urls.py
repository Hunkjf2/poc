from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginUser.as_view(), name="login"), 
    path("criar", views.CreateUsersView.as_view(), name="criar"),
    path("", views.ListarUsersView.as_view(), name=""),
    path("<int:pk>", views.ListarOneUsersView.as_view(), name=""),
    path("editar/<int:id>", views.EditUsersView.as_view(), name="editar"),
    path("delete/<int:id>", views.DeleteUsersView.as_view(), name="delete")
]