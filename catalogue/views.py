from django.shortcuts import render
from .models import Good


def index(request):
    data = dict()
    goods = Good.objects.all()
    data['goods'] = goods
    return render(request, 'catalogue/index.html', context=data)



