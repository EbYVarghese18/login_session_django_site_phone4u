from django.shortcuts import render
from django.http import HttpResponse
from .models import Phones, Tablets, Watches


# Create your views here.
def index(request):
    return render(request, 'index.html')

def phones(request):
    dict_phones = {
        'phones': Phones.objects.all()
    }
    return render(request, 'phones.html', dict_phones)

def tablets(request):
    dict_tablets = {
        'tablets': Tablets.objects.all()
    }
    return render(request, 'tablets.html', dict_tablets)

def watches(request):   
    dict_watches = {
        'watches': Watches.objects.all()
    }
    return render(request, 'watches.html', dict_watches)