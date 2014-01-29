#-*- coding: utf-8 -*-

from time import strftime

from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from users.models import Users


def isLoggedIn(request):
    email = request.COOKIES.get('email')
    token = request.COOKIES.get('token')
    if email and token:
        user = Users.objects.filter(email=email).first()
        print user.email, token
        return user.token == token
    return False



def login(request):
    req = request.GET
    email = req.get('email')
    password = req.get('password')
    user = Users.objects.filter(email=email).first()
    if user and user.password == str(hash(password)):
        token = user.token = str(hash(strftime("%H:%M:%S")))
        user.save()
        response = HttpResponse(
            '{email: \'' + email + '\', token: \'' + str(token) + '\', success: 1} ')
        response.set_cookie('email', email)
        response.set_cookie('token', token)
    else:
        response = HttpResponse('{success: 0}')
    return response


def delete(request):
    return HttpResponse('Not implemented yet.')


def save(request):
    return HttpResponse('Not implemented yet.')
