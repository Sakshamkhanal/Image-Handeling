from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Imageforms

def Image_view(request):

    if request.method == 'POST':
        form = Imageforms(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Imageforms()
    return render(request,'home.html',{'form':form})

def success(request):
    return HttpResponse('sucessfully uploaded')