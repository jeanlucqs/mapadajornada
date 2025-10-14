from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    return render(request, 'index.html')

def pagina_principal(request):
    return render(request, 'principal.html')
    


def pagina_registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
<<<<<<< HEAD
            return redirect('pagina_front')
=======
            return redirect('')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    return render(request, 'index.html')
    
def pagina_registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
>>>>>>> 8d7a46320db8db6fe3c693d59c7a040b1dbc7f68
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


def pagina_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
<<<<<<< HEAD
            return redirect('index')
=======
            return redirect('pagina_principal')

>>>>>>> 8d7a46320db8db6fe3c693d59c7a040b1dbc7f68
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

<<<<<<< HEAD
@login_required
=======
>>>>>>> 8d7a46320db8db6fe3c693d59c7a040b1dbc7f68
def pagina_front(request):
    return render(request, 'pagina_front.html')