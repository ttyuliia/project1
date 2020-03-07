from django.shortcuts import render
from django.http import JsonResponse
from .models import Good
from cart.models import Order


def index(request):
    data = dict()
    goods = Good.objects.all()
    data['goods'] = goods
    return render(request, 'catalogue/index.html', context=data)


def ajax_cart(request):
    response = dict()
    gid = request.GET['gid']
    uid = request.user.id
    sid = 1
    _quantity = 1
    Order.objects.create(quantity=_quantity, status_id=sid, good_id=gid, user_id=uid)
    response['mess'] = f'Заказ успешно сохранен для {request.user.username}'
    return JsonResponse(response)






