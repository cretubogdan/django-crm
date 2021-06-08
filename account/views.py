from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home_view(request):
    return render(request, 'account/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show-view')
    else:
        form = UserCreationForm()

    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    error = ''
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                error = 'Username and password did not match'
            else:
                login(request, user)
                return redirect('show-view')
        except:
            error = "Unknown error"
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form, 'error': error})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home-view')

