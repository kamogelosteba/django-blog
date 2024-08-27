from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django import forms


# User Registration View
class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'members/registration.html'
    success_url = reverse_lazy('login')  # Redirect to login after successful registration


# Custom Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


# Login View using Django's login() function
class LoginPage(View):
    def get(self, request):
        # Display the login form on GET request
        form = LoginForm()
        return render(request, 'members/login.html', {'form': form})

    def post(self, request):
        # Handle login on POST request
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home')  # Redirect to home page after login
            else:
                # Invalid login credentials
                form.add_error(None, "Invalid username or password")

        return render(request, 'members/login.html', {'form': form})
