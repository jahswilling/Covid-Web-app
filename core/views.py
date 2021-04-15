from django.shortcuts import render,redirect,get_object_or_404
import requests
import json

URL = "https://covidnigeria.herokuapp.com/api"


def dashboard(request):

    payload = {}
    files = {}
    headers = {}

    response = requests.request("GET", URL, headers=headers, data = payload, files = files)

    data = json.loads(response.text)
    print(data)

    context = {'data':data}
    return render(request, "index.html",context)
