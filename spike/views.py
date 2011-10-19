from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
import simplejson 
import urllib2

def index(request):
    return render_to_response(
        'index.html', 
        {
            'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID
        }, 
        context_instance=RequestContext(request)
    )
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')
    
def login(request):
    next = '/'
    if 'next' in request.GET:
        next = request.GET['next']
        
    try:
        facebook_cookie_name = 'fbs_' + settings.FACEBOOK_APP_ID
        if facebook_cookie_name in request.COOKIES:
            cookie = request.COOKIES[facebook_cookie_name]
            cookie_info = dict([elem.split('=') for elem in cookie.split('&')])
            uid = cookie_info['uid']
            access_token = cookie_info['access_token']
            
            url = 'https://graph.facebook.com/' + uid + '?access_token=' + access_token
            user_data = simplejson.load(urllib2.urlopen(url))
            
            user = auth.authenticate(username = uid, email = user_data['email'], facebook_name = user_data['name'])
            if user:
                auth.login(request, user)
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(next)
    except:
        return HttpResponseRedirect(next)
                              

