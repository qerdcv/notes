from django import forms

from main.models import Notes


class AddNoteForm(forms.ModelForm):
    note = forms.CharField()

    class Meta:
        model = Notes
        fields = ['user', 'note']

