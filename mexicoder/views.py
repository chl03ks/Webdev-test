from django.shortcuts import render

import requests
import json


def index(request):
    parsedData = []
    if request.method == 'POST':
        search = request.POST.get('search')
        req = requests.get('https://api.github.com/users/' + search)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'mexicoder/index.html', {'data': parsedData})
