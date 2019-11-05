from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from main.forms import AddNoteForm
from main.models import Notes


class Index(generic.FormView):
    form_class = AddNoteForm
    template_name = 'main/main.html'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'notes': Notes.objects.filter(user=self.request.user)})
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


def add_note(request):
    from django.core import serializers
    note = request.GET.get('note')
    Notes.objects.create(user=request.user, note=note)
    return JsonResponse({'id': Notes.objects.filter(user=request.user).last().id})

def remove(request):
    Notes.objects.filter(user=request.user, id=request.POST['id']).delete()
    return JsonResponse({})