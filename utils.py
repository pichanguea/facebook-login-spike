import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import re
import urllib2
import simplejson
from django.conf import settings

def create_facebook_test_user(full_name):
    access_token = get_facebook_app_access_token()
    encoded_full_name = urllib2.quote(full_name)
    url = 'https://graph.facebook.com/%s/accounts/test-users?installed=true&name=%s&permissions=read_stream&method=post&access_token=%s' % (settings.FACEBOOK_APP_ID, encoded_full_name, access_token,)
    result = urllib2.urlopen(url)
    user_data = simplejson.load(result)
    email = user_data['email']
    password = user_data['password']
    return email, password
    
def get_facebook_app_access_token():
    url = 'https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials' % (settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET,)
    result = urllib2.urlopen(url).read()
    
    r = re.match(r'access_token=((\w|\|)+)', result)
    if not r:
        raise ValueError
    access_token = r.groups()[0]
    return access_token
