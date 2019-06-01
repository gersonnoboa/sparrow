#!/usr/bin/env python

import argparse

def start():
  arguments = get_parsed_arguments()
  print(arguments.title)

def get_parsed_arguments():
  parser = argparse.ArgumentParser("sparrow")
  parser.add_argument("title", help="Title of movie or show", type=str)
  arguments = parser.parse_args()
  return arguments


start()
