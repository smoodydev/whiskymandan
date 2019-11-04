from django.forms import ModelForm
from .models import Whiskey, Distiller

# Create the form class.
class WhiskeyForm(ModelForm):
    class Meta:
        model = Whiskey
        fields = ['name', 'distiller', 'blurb', 'bio', 'whiskeyType', 'strength']

class DistillerForm(ModelForm):
    class Meta:
        model = Distiller
        fields = ['name', 'blurb', 'bio']