import urllib
import requests

def get_open_subtitles_search_result(query, episode, season):
  url = get_search_url(query, episode, season)
  headers = {'user-agent': 'TemporaryUserAgent'}
  resp = requests.get(url, headers=headers)

  return resp


def get_search_url(query, episode, season):
  encodedQuery = urllib.parse.quote(query)
  apiURL = []
  apiURL.append('https://rest.opensubtitles.org/search')

  if episode:
    apiURL.append('/episode-%s'%(episode))

  apiURL.append('/query-%s'%(encodedQuery))

  if season:
    apiURL.append('/season-%s'%(season))

  apiURL.append('/sublanguageid-eng')

  return ''.join(apiURL)
