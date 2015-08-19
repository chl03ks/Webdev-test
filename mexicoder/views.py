from __future__ import unicode_literals
from django.shortcuts import render

from twython import Twython


import wikipedia
import urllib

ckey = 'MsT8KiSsk3R7OhotmRCNKKChk'
csecret = 'Wwm9raPcX1FFPktOdsXNqssFCCMAccL3qRhEvqrIxMYMhYWkfh'
atoken = '2585921882-3BDMCj7L7egv2y6Av56syCY12dJsgoNXQP7Akia'
asecret = 'ExtDJrjteOR40zKA3nFii0oHI1WR5XwMJZyWD16TEojKH'

wikipedia.set_lang("fr")

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

    response = urllib.urlopen('http://api.hostip.info/get_html.php?ip=12.215.42.19&position=true').read()
    print(response)
    tweet_list = []
    wiki_list = []
    search = request.GET.get('search', '').strip()
    if search and request.method == 'GET':
        try:
            wiki_topic = wiki_topic = wikipedia.search(search, 15)
        except wikipedia.exceptions.DisambiguationError as e:
            print e.options
        for topic in wiki_topic:
            wiki = dict()
            wiki['topic'] = topic
            wiki_list.append(wiki)
        data = search_twitter(search)
        results = data['statuses']
        for result in results:
            tweet = dict()
            tweet['user'] = result['user']['screen_name']
            tweet['tweet'] = result['text']
            tweet['img_url'] = result['user']['profile_image_url_https']
            tweet_list.append(tweet)

    return render(request, 'mexicoder/index.html', {'data': tweet_list, 'wikidata': wiki_list})
