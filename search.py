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
    apiURL.append(f'/episode-{episode}')

  apiURL.append(f'/query-{encodedQuery}')

  if season:
    apiURL.append(f'/season-{season}')

  apiURL.append('/sublanguageid-eng')

  return ''.join(apiURL)
