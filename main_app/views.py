from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate, logout


# Create your views here.

def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()  # an empty form to display in home page.we can check conditions later (if logged in or not)
    return render(request, 'index.html', {'treasures': treasures, 'form': form})


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
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = form.save(commit=False)
        treasure.user = request.user
        print(treasure.user.id)
        treasure.save()
    return HttpResponseRedirect("/")


def profile(request, username):
    user = User.objects.get(username=username)
    treasure = Treasure.objects.filter(user=user)
    context = {
        'treasures': treasure, 'username': username
    }

    return render(request, 'profile.html', context)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            u_name = login_form.cleaned_data['username']
            u_password = login_form.cleaned_data['password']
            user = authenticate(username=u_name, password=u_password)
            # checking for the user existence and active state
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("User is Not Active")
            else:
                print("Invalid Credentials")


    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def like_treasure(request):
    likes = 0
    treasure_id = request.GET.get('treasure_id', None)
    if (treasure_id):
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()

    return render(likes)
