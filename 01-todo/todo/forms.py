from django import forms
from django.utils import timezone
import datetime

from .models import Todo


class TodoForm(forms.ModelForm):
    # Render the due_date as a native date picker
    due_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Todo
        fields = ["title", "description", "completed", "due_date"]

    def save(self, commit=True):
        obj = super().save(commit=False)
        due = self.cleaned_data.get("due_date")
        if due:
            # combine with midnight and make timezone-aware
            dt = datetime.datetime.combine(due, datetime.time.min)
            if timezone.is_naive(dt):
                dt = timezone.make_aware(dt)
            obj.due_date = dt
        else:
            obj.due_date = None
        if commit:
            obj.save()
        return obj
