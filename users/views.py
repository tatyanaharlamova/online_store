from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
import secrets

from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject="Подтверждение почты",
                  message=f"Перейдите по ссылке для подтверждения почты {url}",
                  from_email='tatyanakharlamova27@yandex.ru',
                  recipient_list=[user.email]
                  )
        return super().form_valid(form)


def email_verification(request, token):
    user = User.objects.get(token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))

