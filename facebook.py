import facepy
import requests
import os
import urlparse

FB_APP_ID = os.environ["FACEBOOK_APP_ID"]
FB_APP_SECRET = os.environ["FACEBOOK_APP_SECRET"]

r = requests.get("https://graph.facebook.com/oauth/access_token?client_id=" + FB_APP_ID + "&client_secret=" + FB_APP_SECRET + "&grant_type=client_credentials")
oauth_access_token = urlparse.parse_qs(str(r.content))['access_token'][0]

print oauth_access_token
