import itertools
from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests

# Create your views here.

def index(request):
    # weather API :
    temp = ''
    icon=''
    if request.method == "POST":
        city = request.POST['city']
        weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=02932c15d8c1e439dbf5fa66cd048d5a" 
        r = requests.get(weather_url.format(city)).json()
        temp = r['main']['temp']
        icon = r['weather'][0]['icon']
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
    # more news :
    more_res = requests.get("https://www.hindustantimes.com/india-news/page/?pageno=2")
    more_soup = bs4.BeautifulSoup(more_res.content, "lxml")
    more_divs = more_soup.find_all('div', attrs={'class':'media-body'})
    more_headlines = []
    more_details = []
    more_times = []
    more_links = []
    for i in range(1, 15):
        heading = more_divs[i].a.text
        more_headlines.append(heading)
        link = more_divs[i].a.get('href')
        more_links.append(link)
        t = more_divs[i].span.text
        more_times.append(t)  
        detail = more_divs[i].find('div', attrs={'class':'para-txt'}).text
        more_details.append(detail)
    return render(request, "news_app/index.html", {'total_cases':total_cases, 'total_deaths':total_deaths, 'total_recovered':total_recovered, 'india_cases':india_cases, 'india_deaths':india_deaths, 'india_recovered':india_recovered, 'headlines':headlines, 'details':details, 'times':times, 'links':links, 'more_headlines':more_headlines, 'more_details':more_details, 'more_times':more_times, 'more_links':more_links, 'temp':temp, 'icon':icon})    


def news_category(request, category):
    url1 = ''
    url2 = ''
    if category == 'education': 
        url1 = 'https://www.hindustantimes.com/education/'
        url2 = 'https://www.hindustantimes.com/education/page/?pageno=2'  # 2nd page url
    elif category == 'international':
        url1 = 'https://www.hindustantimes.com/world-news/'
        url2 = 'https://www.hindustantimes.com/world-news/page/?pageno=2'  # 2nd page url
    elif category == 'regional':
        url1 = 'https://www.hindustantimes.com/cities/'
        url2 = 'https://www.hindustantimes.com/cities/page/?pageno=2'  # 2nd page url
    elif category == 'medical':
        url1 = 'https://www.hindustantimes.com/health/'
        url2 = 'https://www.hindustantimes.com/health/page/?pageno=2'  # 2nd page url
    elif category == 'economy':
        url1 = 'https://www.hindustantimes.com/real-estate/'
        url2 = 'https://www.hindustantimes.com/real-estate/page/?pageno=2'  # 2nd page url
    elif category == 'sports':
        url1 = 'https://www.hindustantimes.com/sports-news/'
        url2 = 'https://www.hindustantimes.com/sports-news/page/?pageno=2'  # 2nd page url
    elif category == 'business':
        url1 = 'https://www.hindustantimes.com/business-news/'
        url2 = 'https://www.hindustantimes.com/business-news/page/?pageno=2'  # 2nd page url
    elif category == 'entertainment':
            url1 = 'https://www.hindustantimes.com/entertainment/'
            url2 = 'https://www.hindustantimes.com/entertainment/page/?pageno=2'  # 2nd page url
    res3 = requests.get(url1)
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
    # more news :
    more_res = requests.get(url2)
    more_soup = bs4.BeautifulSoup(more_res.content, "lxml")
    more_divs = more_soup.find_all('div', attrs={'class':'media-body'})
    more_headlines = []
    more_details = []
    more_times = []
    more_links = []
    for i in range(1, 15):
        heading = more_divs[i].a.text
        more_headlines.append(heading)
        link = more_divs[i].a.get('href')
        more_links.append(link)
        t = more_divs[i].span.text
        more_times.append(t)  
        detail = more_divs[i].find('div', attrs={'class':'para-txt'}).text
        more_details.append(detail)
    return render(request, "news_app/news_category.html", {'category':category, 'headlines':headlines, 'details':details, 'times':times, 'links':links, 'more_headlines':more_headlines, 'more_details':more_details, 'more_times':more_times, 'more_links':more_links})


def test(request):
    return render(request, "news_app/test.html")