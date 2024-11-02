from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from account.forms.CustomUserLoginForm import CustomUserLoginForm
from account.forms.CustomUserRegisterForm import CustomUserRegisterForm
from django.shortcuts import render, redirect

# Vue pour l'inscription
def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre inscription est OK')
            return redirect('login')
    else:
        form = CustomUserRegisterForm()
    
    return render(request, 'account/register.html', {'form': form})

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Connexion de l'utilisateur
                messages.success(request, 'Vous êtes connecté maintenant')
                return redirect('home')
            else:
                messages.error(request, 'Votre mot de passe ou votre nom est incorrect')
    else:
        form = CustomUserLoginForm()
    
    return render(request, 'account/login.html', {'form': form})

# Vue pour la déconnexion
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Vous êtes déconnecté avec succès')
    return redirect('login')
