#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import argparse

def main():
  parser = argparse.ArgumentParser(description='Exercise bing translation api.')
  parser.add_argument('user', help='username.', type=str)
  parser.add_argument('password', help='password.', type=str)
  args = parser.parse_args()

  user = args.user
  password = args.password

  payload = {
    'channel' : '#/jp/shows',
    'nick' : 'on-three',
    'url' : 'www.jisho.org',
    'kanji' : '何処',
    'romaji' : 'doko',
    'kana' : 'どこ',
    'text' : 'where',
    'word' : 'doko',
    }
  headers = {'content-type': 'application/json'}

  r = requests.post("http://127.0.0.1/jisho/api/", 
      auth=(user,password),
      data=json.dumps(payload),headers=headers)

  print r.json

if __name__ == "__main__":
  main()
