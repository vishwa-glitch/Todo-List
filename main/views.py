from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from .models import Item, ToDoList
from .forms import TaskForm
from django.contrib.auth import logout

# View for the homepage that displays user's to-do lists
@login_required
def combined_view(request):  # home
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    
    # Retrieve all to-do lists for the current user, ordered by ID (most recent first)
    todolists = request.user.todolist.all().order_by('-id')
    
    if request.method == "POST":
        # Get the list ID from the POST data
        list_id = request.POST.get("list_id")
        
        if list_id:
            # Get the specific to-do list for the current user, or return a 404 if not found
            todolist = get_object_or_404(ToDoList, id=list_id, user=request.user)
            
            # Handle saving changes to items (marking them as complete or incomplete)
            if "save" in request.POST:
                for item in todolist.items.all():
                    item_id = str(item.id)
                    if f"c{item_id}" in request.POST:
                        item.complete = True  # Mark item as complete if it's checked
                    else:
                        item.complete = False  # Mark item as incomplete if it's unchecked
                    item.save()
            
            # Handle adding new items to the to-do list
            elif "new_item" in request.POST:
                new_item_text = request.POST.get(f"new_item_{list_id}").strip()
                if new_item_text:
                    todolist.items.create(text=new_item_text, complete=False)  # Create a new item
                else:
                    # Optionally, add an error message if the item text is empty
                    pass
    
    # Render the home page with the user's to-do lists
    return render(request, "main/home.html", {"todolists": todolists})

# View to create a new to-do list
@login_required
def create_todolist(request):  # create
    if request.method == "POST":
        # If the form is submitted, process the data
        form = TaskForm(request.POST)
        if form.is_valid():
            # Save the new to-do list, but don't commit to the database yet
            todolist = form.save(commit=False)
            todolist.user = request.user  # Assign the current user to the to-do list
            todolist.save()  # Save the to-do list to the database
            return redirect('combined_view')  # Redirect to the home page
    else:
        # If the request method is GET, create an empty form
        form = TaskForm()
    
    # Render the create to-do list page with the form
    return render(request, 'main/create.html', {'form': form})

# View to log out the user
@login_required
def logout_view(request):
    logout(request)  # Log out the current user
    return render(request, 'main/logout.html')  # Render a logout confirmation page
