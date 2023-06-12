from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import Profile


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class MyLogoutView(LogoutView):
    """ CBV для выхода из аккаунта """
    
    next_page = reverse_lazy("myauth:login")
    
    
class RegisterView(CreateView):
    """ CBV для регистрации нового аккаунта """
    
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy("myauth:about-me")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response