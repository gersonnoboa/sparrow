#!/usr/bin/env python
from argument_parsing import get_parsed_arguments
from search import get_open_subtitles_search_result
from json_parsing import parse_json
from subtitles_presenter import get_subtitle_from_user

def start():
  arguments = get_parsed_arguments()
  request = get_open_subtitles_search_result(arguments.title, arguments.episode, arguments.season)
  movies = parse_json(request.json())
  subtitle = get_subtitle_from_user(movies)

  if subtitle:
    print(subtitle.srt_name)


start()
