from django.shortcuts import render
from .models import myForm
from .forms import RegistrationForm

# Create your views here.

def index(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['uname']
            dt = form.cleaned_data['title']
            desc = form.cleaned_data['description']

            reg = myForm(uname=nm, title=dt, description=desc)
            reg.save()
            form = RegistrationForm()
    else:
        form = RegistrationForm()
        
    return render(request, 'myform/index.html', {'form':form})
