#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from news.models import News


def home(request):
    if request.GET.get('id'):
        newsId = request.GET.get('id')
        news = News.objects.filter(id=newsId)

    else:
        news = News.objects.all().order_by('date').reverse()[:20]

    return HttpResponse(serialize('json', news))


def delete(request):
    newsId = request.GET.get('id')
    if newsId:
        # Check if logged in !
        news = News.objects.filter(id=newsId)
        news.delete()
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def save(request):
    # Check if logged in !
    req = request.GET
    id = req.get('id')
    title = req.get('title')
    content = req.get('content')
    mag = req.get('mag')
    if id:
        news = News.objects.filter(id=id)
        news = news.first()
    else:
        news = News()
    news.title = title
    news.content = content
    news.mag = mag
    news.save()
    return HttpResponse('1')