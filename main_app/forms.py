# forms.py

from django.forms import ModelForm
from .models import Cleaner

class CleanerForm(ModelForm):
  class Meta:
    model = Cleaner
    fields = ['make']
