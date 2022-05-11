from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registerView),
    path('login/', views.userLoginView),
    path('todo/', views.todolistView),
    path('edit/<int:id>/', views.editTodoList),
    path('delete/<int:id>/', views.deleteTodo),
    path('update/', views.updateTodoList),
]
