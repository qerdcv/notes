import logging

from django.views import generic
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from main.forms import AddNoteForm
from main.models import Notes


logger = logging.getLogger(__name__)


class Index(generic.FormView):
    form_class = AddNoteForm
    template_name = 'main/main.html'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user == 'AnonymousUser':
            context.update({'notes': Notes.objects.filter(user__username=self.request.user.username).order_by('id')})
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super().form_valid(form)


class UserCreating(generic.FormView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
