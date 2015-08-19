from __future__ import unicode_literals
from django.shortcuts import render

from twython import Twython

import requests
import json

ckey = 'MsT8KiSsk3R7OhotmRCNKKChk'
csecret = 'Wwm9raPcX1FFPktOdsXNqssFCCMAccL3qRhEvqrIxMYMhYWkfh'
atoken = '2585921882-3BDMCj7L7egv2y6Av56syCY12dJsgoNXQP7Akia'
asecret = 'ExtDJrjteOR40zKA3nFii0oHI1WR5XwMJZyWD16TEojKH'


twitter = Twython(ckey, csecret, atoken, asecret)


def search_twitter(search_term, geocode=None):
    twitter = Twython(ckey, csecret)
    if geocode:
        result_search = twitter.search(q=search_term, geocode=geocode)
    else:
        result_search = twitter.search(q=search_term)
    return result_search


def utf8ify(list):
    '''Encode a list of strings in utf8'''
    return [item.encode('utf8') for item in list]


def index(request):
    tweet_list = []
    if request.method == 'POST':
        search = request.POST.get('search')
        req = requests.get('https://api.github.com/users/' + search)
        jsonList = []
        jsonList.append(json.loads(req.content))
        data = search_twitter(search)
        results = data['statuses']
        for result in results:
            tweet = dict()
            tweet['user'] = result['user']['screen_name']
            tweet['tweet'] = result['text']
            tweet['img_url'] = result['user']['profile_image_url_https']
            tweet_list.append(tweet)
    return render(request, 'mexicoder/index.html', {'data': tweet_list})
