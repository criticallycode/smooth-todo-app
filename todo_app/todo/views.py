from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo.html/', {'all_items': todo_items})

def addToDo(request):
    # create a new to-do item and add it to the list of all items
    new_item = TodoItem(content = request.POST['content'])
    # save the new item
    new_item.save()
    # redirect to the original url
    return HttpResponseRedirect('/todo/')

def deleteToDo(request, todo_id):
    item_for_deletion = TodoItem.objects.get(id=todo_id)
    item_for_deletion.delete()
    # redirect to the original url
    return HttpResponseRedirect('/todo/')