from django.shortcuts import render
from app.forms import *

# Create your views here.
def write(request):
    form = Form()
    return render(request, 'write.html', {'form':form})