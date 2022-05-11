from django.shortcuts import render
from .models import UserRegister, UserLogin, TodoList


def registerView(req):
    if req.method == 'POST':
        data = req.POST
        reg = UserRegister(username=data['username'], email=data['email'], password=data['password'])
        reg.save()
        return render(req, 'register.html')
    return render(req, 'register.html')


def userLoginView(req):
    if req.method == 'POST':
        data = req.POST
        user = data['username']
        pass1 = data['password']
        reg = UserLogin(username=user, password=pass1)
        reg.save()
    msg = 'User Registration Sucessfully'
    return render(req, 'login.html', {'msg': msg})


def todolistView(req):
    if req.method == 'POST':
        data = req.POST
        reg = TodoList(text=data['todolist'])
        reg.save()
        return render(req, 'todolist.html', {'regs': TodoList.objects.all(), 'reg': reg})
    else:
        return render(req, 'todolist.html', {'regs': TodoList.objects.all()})


def editTodoList(req, id):
    reg = TodoList.objects.get(id=id).delete()
    return render(req, 'edit.html')


def updateTodoList(req):
    if req.method == 'POST':
        totext = req.POST['todolist']
        reg = TodoList(text=totext)
        reg.save()
        return render(req, 'todolist.html', {'reg': reg})
    else:
        return render(req, 'todolist.html', {'regs': TodoList.objects.all()})


def deleteTodo(req, id):
    reg = TodoList.objects.get(id=id)
    reg.delete()
    msg = 'Todo delete successfully'
    return render(req, 'todolist.html', {'msg': msg, 'regs': TodoList.objects.all()}, )
