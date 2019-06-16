#!/usr/bin/env python
from argument_parsing import get_parsed_arguments
from search import get_open_subtitles_search_result
from json_parsing import parse_json
from subtitles_presenter import present_subtitles

def start():
  arguments = get_parsed_arguments()
  request = get_open_subtitles_search_result(arguments.title, arguments.episode, arguments.season)
  movies = parse_json(request.json())
  present_subtitles(movies)


start()
