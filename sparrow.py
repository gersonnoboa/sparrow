#!/usr/bin/env python#

from argument_parsing import get_parsed_arguments
from search import get_open_subtitles_search_result
from json_parsing import parse_json
from subtitles_presenter import get_subtitle_from_user
from file_downloader import download_file
from rename_file import rename_file

def start():
  arguments = get_parsed_arguments()
  request = get_open_subtitles_search_result(arguments.title, arguments.episode, arguments.season)
  subtitles = parse_json(request.json())

  if len(subtitles.subtitles) == 0:
    print("No subtitles for that query. Please try again with a new query.")
    return

  subtitle = get_subtitle_from_user(subtitles)

  if subtitle:
    new_subtitle_name = f'{subtitle.release_name}.eng.srt'

    if not rename_file(subtitle.release_name):
      print("Error renaming video file")
      return

    if not download_file(subtitle.zip_download_link, new_subtitle_name):
      print("Error downloading subtitle")
      return

    print('Operations completed successfully.')


start()
