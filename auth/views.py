from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .forms import SignupForm, LoginForm


class HomeView(TemplateView):
    template_name = 'home.html'


class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm


class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(SignupView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid