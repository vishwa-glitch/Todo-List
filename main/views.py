from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from .models import Item, ToDoList
from .forms import TaskForm
from django.contrib.auth import logout

# Create your views here.
@login_required
def combined_view(request):  # home
    if not request.user.is_authenticated:
        return redirect('login')  # Make sure this matches the name in your urls.py
    todolists = request.user.todolist.all().order_by('-id')
    if request.method == "POST":
        list_id = request.POST.get("list_id")
        if list_id:
            todolist = get_object_or_404(ToDoList, id=list_id, user=request.user)
            if "save" in request.POST:
                for item in todolist.items.all():
                    item_id = str(item.id)
                    if f"c{item_id}" in request.POST:
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif "new_item" in request.POST:
                new_item_text = request.POST.get(f"new_item_{list_id}").strip()
                if new_item_text:
                    todolist.items.create(text=new_item_text, complete=False)
                else:
                    # You could add an error message here if needed
                    pass
    
    return render(request, "main/home.html", {"todolists": todolists})

@login_required
def create_todolist(request):  # create
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.user = request.user
            todolist.save()
            return redirect('combined_view')
    else:
        form = TaskForm()
    
    return render(request, 'main/create.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'main/logout.html') 

