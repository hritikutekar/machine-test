from django.contrib import admin
from .models import TodoList, UserLogin, UserRegister


class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
admin.site.register(UserRegister, UserRegisterAdmin)


class UserLoginAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']
admin.site.register(UserLogin, UserLoginAdmin)


class TodoListAdmin(admin.ModelAdmin):
    list_display = ['text']
admin.site.register(TodoList, TodoListAdmin)
