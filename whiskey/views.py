from django.shortcuts import render, redirect, get_object_or_404
from .models import Whiskey, Distiller
from .forms import DistillerForm, WhiskeyForm

# Create your views here.

def add_distiller(request):
    if request.method=="POST":
        form = DistillerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("whiskeys")
    else:
        form = DistillerForm()
    return render(request, 'add_form_base.html', {"form":form})

def add_whiskey(request):
    if request.method=="POST":
        form = WhiskeyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("whiskeys")
    else:
        form = WhiskeyForm()
    return render(request, 'add_form_base.html', {'form': form})

def all_whiskeys(request):
    whiskeys = Whiskey.objects.all()
    return render(request, 'all_whiskeys.html', {"whiskeys":whiskeys})

def get_whiskey(request, id):
    whiskey = get_object_or_404(Whiskey, pk=id)
    return render(request, 'whiskey.html', {"whiskey":whiskey})

def get_distiller(request, id):
    whiskey = get_object_or_404(Distiller, pk=id)
    return render(request, 'whiskey.html', {"whiskey":whiskey})

