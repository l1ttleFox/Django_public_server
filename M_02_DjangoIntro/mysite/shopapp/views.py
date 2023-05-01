from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer
import datetime


def shop_index(request: HttpRequest) -> object:
    context = {
        "time_running": round(default_timer()),
        "new_year": datetime.datetime(2024, 1, 1, hour=0, minute=0, second=0, microsecond=0),
        "now": datetime.datetime.now()
    }
    return render(request, 'shopapp/shop-index.html', context=context)
