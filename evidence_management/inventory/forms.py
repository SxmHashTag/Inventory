from django import forms
from .models import Case, Evidence

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'number', 'hovj', 'team']

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['description', 'collected_on', 'added_by']
