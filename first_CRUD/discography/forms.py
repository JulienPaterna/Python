from django.forms import ModelForm
from .models import Disc

class DiscForm(ModelForm):
    class Meta:
        model = Disc
        fields = ['Picture', 'Title','Artist', 'Release_Year', 'Format']       