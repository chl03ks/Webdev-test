from __future__ import unicode_literals
from django.shortcuts import render

from twython import Twython


import wikipedia
import urllib

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


def index(request):
    """
    Twiiter and Wikipedia API Call
    """
    tweet_list = []
    wiki_list = []
    search = request.GET.get('search', '').strip()
    if search and request.method == 'GET':
        try:
            if request.GET.get('lag') and request.GET.get('log'):
                lag = request.GET.get('lag')
                log = request.GET.get('log')
                wiki_topic = wikipedia.geosearch(lag, log, search)
            else:
                wiki_topic = wikipedia.search(search, 15)
        except wikipedia.exceptions.DisambiguationError as e:
            print e.options
        for topic in wiki_topic:
            wiki = dict()
            wiki['topic'] = topic
            wiki_list.append(wiki)

        if request.GET.get('lag') and request.GET.get('log'):
            lag = request.GET.get('lag')
            log = request.GET.get('log')
            data = search_twitter(search, lag + ',' + log + ',100mi')
        else:
            data = search_twitter(search)

        results = data['statuses']

        for result in results:
            tweet = dict()
            tweet['user'] = result['user']['screen_name']
            tweet['tweet'] = result['text']
            tweet['img_url'] = result['user']['profile_image_url_https']
            tweet_list.append(tweet)

    return render(request, 'mexicoder/index.html', {'data': tweet_list, 'wikidata': wiki_list})
