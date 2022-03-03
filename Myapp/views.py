from django.shortcuts import render
from .forms import form_render
from .models import Image
# Create your views here.
def home(request):
    form = form_render()
    return render(request,'home.html',{'form':form})