from django.shortcuts import render
from django.http import HttpResponse
# import requests
import json


def getapi(requests):
    url="/trainee/list/"
    head = {'contnet-type': 'application/json'}
    res = requests.get(url=url, headers=head)
    print(res.json())
    return HttpResponse("get")

def postapi(requests):
    url = "/trainee/insert/"
    header = {
        "Content-Type": "application/json",
    }
    data = {
        "name": "sara",
        "brnach": "3",
        "courses": "1",
    }
    result = requests.post(url=url, data=json.dumps(data), headers=header)
    if result.status_code == 200:
        return HttpResponse('saved data')
    return HttpResponse('error try again')
