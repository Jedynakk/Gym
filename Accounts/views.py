
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from Accounts.forms import LoginForm, AddUserForm


class LoginView(View):
    def get(self, request):
        return render(request, 'Accounts/login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                return redirect('main_page')
        return render(request, 'Accounts/login.html', {'form': LoginForm()})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'Accounts/add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_staff = False
            user.save()
            return redirect('login')
        return render(request, 'Accounts/add_user.html', {'form': form})