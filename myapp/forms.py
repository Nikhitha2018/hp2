from django import forms 
# forms.py 
from .models import Black
class BlackForm(forms.ModelForm):
    class Meta:
        model=Black
        fields='__all__'
