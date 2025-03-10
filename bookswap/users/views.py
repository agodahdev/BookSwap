from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in new user
            return redirect('book_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})