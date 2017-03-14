from django.shortcuts import render
from .models import Treasure
from .forms import TreasureForm
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    treasures = Treasure.objects.all()
    form=TreasureForm()#an empty form to display in home page.we can check conditions later (if logged in or not)
    return render(request, 'index.html', {'treasures': treasures,'form':form})


def detail(request, treasure_id):
    treasures = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasures})


# def post_treasure(request):
#     form = TreasureForm(request.POST)
#     if form.is_valid():
#         treasure = Treasure(name=form.cleaned_data['name'],
#                             value=form.cleaned_data['value'],
#                             location=form.cleaned_data['location'],
#                             material=form.cleaned_data['material'],
#                             img_url=form.cleaned_data['img_url'])
#         # don't forget to save
#         treasure.save()
#         return HttpResponseRedirect("/")
'''
we can do the same stuff in simple steps using
'''

def post_treasure(request):
    form=TreasureForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return HttpResponseRedirect("/")