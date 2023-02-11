from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from.models import Sneaker
from.forms import CleanerForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneakers_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakers':sneakers})

def sneakers_detail(request,sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    cleaner_form = CleanerForm()
    return render(request, 'sneakers/detail.html', {'sneaker':sneaker, 'cleaner_form':cleaner_form})

...

def add_cleaner(request, sneaker_id):
  form = CleanerForm(request.POST)
  return redirect('detail',sneaker_id=sneaker_id)



class SneakerCreate(CreateView):
    model=Sneaker
    fields = '__all__'
    sucess_url = '/sneakers'

class SneakerUpdate(UpdateView):
    model= Sneaker
    fields ='__all__'

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/'



