from django.forms import ModelForm
from .models import Lead

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['title', 'contact', 'end', 'rate', 'currency', 'jd', 'active', 'next_step']