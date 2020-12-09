from django.conf import settings
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView

from .forms import UpdateUserForm, UserRegisterForm


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class LoginView(generic.View):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, "home.html")


class LogoutView(generic.RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
            logout(self.request)
            return reverse('home')
            
class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateUserForm
    template_name = 'registration/update_user.html' 

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, instance = request.user)
        context = {'form': form}
        return render(request, 'registration/update_user.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance = request.user)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, 'registration/update_user.html', context )

class UpdatePasswordView(LoginRequiredMixin, generic.FormView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html' 

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, user = request.user)
        context = {'form': form}
        return render(request, 'registration/change_password.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, user = request.user)
        context = {'form': form}
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/')

        return render(request, 'registration/change_password.html', context )

