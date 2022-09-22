from itertools import count
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist_html(request):
    return render(request, "mywatchlist.html",context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchList.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = MyWatchList.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

data_watchlist_items = MyWatchList.objects.all()

context = {
    'list_item': data_watchlist_items,
    'name': 'Muhammad Alif Ismady',
    
}

