from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from .models import Advertisement, User
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
import os

`


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title=title)
    else:
        advertisements = Advertisement.objects.all()

    context = {
        "advertisements": advertisements,
        "title": title
    }

    return render(request, "index.html", context)
def top_sellers(request):
    user = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context ={'users':user}
    return render(request, 'top-sellers.html',context)
@login_required(login_url=reverse_lazy("login"))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
def regist(request):
    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return render(request, 'registr.html', data)
    else:
        form = UserCreationForm()
        data['form'] = form
        return render(request, 'registr.html', data)
def advertisement_detail(request, pk):
    advertisement=Advertisement.objects.get(id=pk)
    context={"adv":advertisement}
    return render(request,'advertisement.html',context)
