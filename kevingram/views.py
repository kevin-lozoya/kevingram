"""Kevingram views."""

# Utilities
from datetime import datetime
import json

# Django
from django.http import HttpResponse

def hello(request):
    """Return the hello's view"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Current time server is: {}'.format(now))


def sorted(request):
    """Return a JSON response with sorted integers"""
    numbers = request.GET['numbers'].split(',')
    numbers = [int(i) for i in numbers]
    data = {
        'status': 'ok',
        'numbers': sorted(numbers),
        'message': 'Integers sorted successfully'
    }
    # import pdb;pdb.set_trace()
    return HttpResponse(
        json.dumps(data),
        content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here.'.format(name)
    else:
        message = 'Hi, {}!. Wellcome to Kevingram.'.format(name)

    return HttpResponse(message)

