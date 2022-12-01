import os
from django.shortcuts import render, HttpResponse
from .forms import DateForm
import datetime
import requests


def nasa_api(request):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = request.POST['date']
    else:
        form = DateForm()

    url = "https://api.nasa.gov/planetary/apod"
    api_key = "q83Psprq7yVHZbffIbbGpQ6p3hMuFnlB56fAEUb3"
    headers = {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
    response = requests.get(url, headers=headers, params={"api_key": api_key, "date": date})
    url_img = response.json()["url"]
    date_str = datetime.datetime.fromisoformat(date).strftime("%d.%m.%Y")
    return render(request, 'autoholl/webform.html', {'form': form, "url_img": url_img, "date_str": date_str})

