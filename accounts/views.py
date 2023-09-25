from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

User = get_user_model()


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('tasks')


def user_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(request, username=username, password=password)
            if new_user is not None:
                if new_user.is_active:
                    login(request, new_user)
            return redirect('tasks')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


