from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta: # additional information 
        model = Feeding
        fields = ['date','meal']