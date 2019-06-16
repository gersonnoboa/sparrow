import argparse


def get_parsed_arguments():
  parser = argparse.ArgumentParser('sparrow')
  parser.add_argument('-t', dest="title", required=True,
                      help='Title of movie or show', type=str)
  parser.add_argument('-e', dest="episode", required=False,
                      help='Episode of show within the season', type=int)
  parser.add_argument('-s', dest="season", required=False,
                      help='Episode', type=int)
  arguments = parser.parse_args()
  return arguments
