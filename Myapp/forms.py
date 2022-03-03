from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Image

class form_render(forms.Modelform):
    class meta:
        model = Image
        fields = "__all__"


