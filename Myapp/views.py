from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.
def home(request):
    form = ImageForm()
    return render(request,'home.html')