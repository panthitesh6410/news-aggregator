import itertools
from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests

# Create your views here.

def index(request):
    # covid-19 cases :
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
    # getting news-headline, deatails and time :
    res3 = requests.get("https://www.hindustantimes.com/india-news/")
    soup3 = bs4.BeautifulSoup(res3.content, "lxml")
    ul = soup3.find('ul', attrs={'class':'latest-news-morenews more-latest-news more-separate newslist-sec'})
    divs = ul.find_all('div', attrs={'class':'media'})
    headlines = []
    details = []
    times = []
    links = []
    for div in divs:
        heading3 = div.find('div', attrs={'class':'media-heading headingfour'}).text
        headlines.append(heading3)
        p3 = div.find('p').text
        details.append(p3)
        time = div.find('span',attrs={'class':'time-dt'}).text
        times.append(time)
        a = div.find('a').get('href')
        links.append(a)
    return render(request, "news_app/index.html", {'total_cases':total_cases, 'total_deaths':total_deaths, 'total_recovered':total_recovered, 'india_cases':india_cases, 'india_deaths':india_deaths, 'india_recovered':india_recovered, 'headlines':headlines, 'details':details, 'times':times, 'links':links})    
