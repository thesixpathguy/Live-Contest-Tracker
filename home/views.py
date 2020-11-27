from django.shortcuts import render, HttpResponse, redirect
import json
import requests


# Create your views here.

def index(request):
    url = "https://www.kontests.net/api/v1/all"
    response = requests.get(url)
    js = json.loads(response.text)
    lst = list()
    lst1 = list()
    for contest in js:
        temp = dict()
        temp['name'] = contest['name']
        temp['link'] = contest['url']
        if (contest['duration'] != '-'):
            temp['duration'] = str(float(contest['duration'])//60)+" minutes"
        else:
            temp['duration'] = "Not Available"
        temp['site'] = contest['site']
        temp['status'] = contest['status']
        if (contest['start_time'] != '-'):
            st = contest['start_time']
            date = st[0:10]
            time = st[11:19]
            temp['date'] = date
            temp['time'] = time
        else:
            temp['date'] = "Not Available"
            temp['time'] = 'Not Available'
        if (contest['end_time'] != '-'):
            st = contest['end_time']
            date = st[0:10]
            time = st[11:19]
            temp['edate'] = date
            temp['etime'] = time
        else:
            temp['edate'] = "Not Available"
            temp['etime'] = 'Not Available'
        if (temp['status'] == 'CODING'):
            lst.append(temp)
        else:
            lst1.append(temp)
    context = {'runnings': lst, 'futures': lst1}
    return render(request, 'j.html', context)


def about(request):
    return render(request, 'about.html')
