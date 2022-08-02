from urllib import request
from django.http import HttpResponse, JsonResponse


def http_test(request):
    #return HttpResponse('this is a test')
    return HttpResponse('<h1>this is a test</h1>')

def json_test(request):
    return JsonResponse({'name':'saneli'})