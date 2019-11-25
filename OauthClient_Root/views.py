# -*- coding: utf-8 -*-
import requests
from requests_oauthlib import OAuth2Session
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse

oauth_server = 'http://sso.wisp.net:8000'
client_id = "MWwEP6UEcnLMuHhjp4j5PVwEznrrw9BmKglotZi2"
client_secret = "37lI6B4TxrdMY1nyulvioubbLvyUiS2L7bJ9vfN0qpNPweU62M9J0GXGcyocX7TzvubVrqjjAE3EM2CThlJTiDHtTk0bHP2WvzTsMlh7jWIHDmo9qZGAY0ZyGyS8a0tI"
authorization_base_url = oauth_server + '/o/authorize/'
token_url = oauth_server + '/o/token/'


def login_oauth(request):
    if 'oauth_token' in request.session:
        return redirect(request.GET['next'])
    oauth_session = OAuth2Session(client_id, )
    authorization_url, state = oauth_session.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    request.session['oauth_state'] = state
    return redirect(authorization_url)


def callback(request):
    oauth_sate = request.GET['state']
    oauth_session = OAuth2Session(client_id, state=oauth_sate)
    token = oauth_session.fetch_token(token_url, client_secret=client_secret, code=request.GET['code'])
    request.session['oauth_token'] = token
    return redirect(reverse('saldo'))


def saldo(request):
    if 'oauth_token' in request.session:
        token = request.session['oauth_token']
        headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}
        secure_users_url = oauth_server + '/users/'
        r = requests.get(secure_users_url, headers=headers)
        html = "<html><body>" + r.content + "</body></html>"
        return HttpResponse(html)
    else:
        return redirect('/login/?next=/saldo/')

