from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from music_services.accounts.forms import UserRegisterForm
from music_services.accounts.models import AppUser
from music_services.web.models import Service, Recommendation

UserModel = get_user_model()


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/account-login.html'


class UserRegisterView(views.CreateView):
    model = AppUser
    template_name = 'accounts/account-register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        try:
            login(request, self.object)
        except AttributeError as ex:
            return render(request, '500-email-username-exist.html')
        return response


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/account-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['services'] = Service.objects.filter(user__exact=self.request.user)
        context['recommendations'] = Recommendation.objects.filter(user__exact=self.request.user)

        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/account-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'profile_picture')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/account-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')
