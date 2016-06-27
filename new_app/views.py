from django.shortcuts import render
import json
from collections import OrderedDict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def home(request):
    x = json.loads(request.body)
    y = x.get('string')
    z = y.split()
    result = [i.strip(',.') for i in z]
    output = OrderedDict()
    for i in result:
        output[i] = result.count(i)
    return HttpResponse(json.dumps(output),content_type='application/json')
