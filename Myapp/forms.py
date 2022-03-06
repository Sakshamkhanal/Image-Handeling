from socket import fromshare
from django.forms import ModelForm
from .models import Image

class Imageforms(ModelForm):
    class Meta:
        model = Image
        fields =['text','photo']

