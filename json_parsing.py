from classes import *


def parse_json(json):
  min_value = min(len(json), 20)
  subtitlesList = list()

  for index in range(1, min_value):
    row = json[index]
    subtitlesList.append(get_subtitle_from_row(row))

  movies = Subtitles(subtitlesList)

  return movies


def get_subtitle_from_row(row):
  release_name = row["MovieReleaseName"]
  srt_name = row["SubFileName"]
  zip_download_link = row["ZipDownloadLink"]
  score = row["Score"]
  download_count = row["SubDownloadsCnt"]

  subtitle = Subtitle(release_name,
                      srt_name,
                      zip_download_link,
                      score,
                      download_count)

  return subtitle
