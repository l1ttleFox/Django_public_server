from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from .models import Profile


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})


class ProfileUpdateView(UpdateView):
    """ CBV для обновления профиля. """
    
    model = Profile
    fields = "bio", "avatar"
    template_name_suffix = "_update"
    
    def get_success_url(self):
        return reverse("myauth:about-me")
    
    def get(self, request, *args, **kwargs):
        print(self.get_object().pk)
        print(request.user.pk)
        if request.user.is_staff or (self.get_object().user.pk == request.user.pk):
            return super().get(request, args, kwargs)
        else:
            raise PermissionDenied

    
def about_me_update_redirect_view(request: HttpRequest) -> HttpResponse:
    """ View-функция для редиректа с about-me/update на уникальную ссылку."""
    
    return redirect(reverse("myauth:update_profile", kwargs={"pk": request.user.profile.pk}))


class UserListView(ListView):
    """ CBV для отображения списка пользователей. """
    
    template_name = 'myauth/user_list.html'
    model = User
    context_object_name = "users"
    
    
class UserDetailView(DetailView):
    """ CBV для отображения деталей пользователя. """
    
    template_name = 'myauth/user_details.html'
    model = User
    context_object_name = "user_details"
    