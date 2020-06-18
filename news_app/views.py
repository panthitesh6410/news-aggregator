from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests

# Create your views here.

def index(request):
    res1 = requests.get("https://www.worldometers.info/coronavirus/")
    soup1 = bs4.BeautifulSoup(res1.text, 'lxml')
    total = soup1.find_all('div', attrs={'class':'maincounter-number'})
    total_cases = total[0].text
    total_deaths = total[1].text
    total_recovered = total[2].text
    res2 = requests.get("https://www.worldometers.info/coronavirus/country/india/")
    soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
    india = soup2.find_all('div', attrs={'class':'maincounter-number'})
    india_cases = india[0].text
    india_deaths = india[1].text
    india_recovered = india[2].text
    return render(request, "news_app/index.html", {'total_cases':total_cases, 'total_deaths':total_deaths, 'total_recovered':total_recovered, 'india_cases':india_cases, 'india_deaths':india_deaths, 'india_recovered':india_recovered})

