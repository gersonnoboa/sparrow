#!/usr/bin/env python

import argparse
import urllib
import requests

def start():
  arguments = get_parsed_arguments()
  request = get_open_subtitles_search_result(arguments.title)
  json = request.json()

  print(len(json))


def get_parsed_arguments():
  parser = argparse.ArgumentParser('sparrow')
  parser.add_argument('title', help='Title of movie or show', type=str)
  arguments = parser.parse_args()
  return arguments


def get_open_subtitles_search_result(query):  
  url = get_search_url(query)
  headers = {'user-agent': 'TemporaryUserAgent'}
  resp = requests.get(url, headers=headers)

  return resp


def get_search_url(query):
  encodedQuery = urllib.parse.quote(query)
  apiBaseURL = f'https://rest.opensubtitles.org/search/query-{encodedQuery}/sublanguageid-eng'
  
  print(apiBaseURL)
  return apiBaseURL


start()
