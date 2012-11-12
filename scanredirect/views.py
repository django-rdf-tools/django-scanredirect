#!/usr/bin/env python
# -*- coding:utf-8 -*
from django.shortcuts import redirect


def back_home(request):
    client_address = request.META['REMOTE_ADDR']
    if client_address in ['127.0.0.1', 'localhost']:
        client_address = request.META.get('HTTP_X_FORWARDED_FOR',
                                          'www.randomwebsite.com/cgi-bin/random.pl')
    return redirect('http://' + client_address)
