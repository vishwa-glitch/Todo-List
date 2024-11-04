from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            return redirect("create")  # Redirect to a different page after login (replace 'home' with your actual URL)
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {'form': form})
