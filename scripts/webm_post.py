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
            'channel': '#/jp/shows', 
            'nick': 'on_three', 
            'url': 'https://www.youtube.com/watch?v=02XG5zfpSCY', 
            'filename': 'xxx.webm', 
            'name': 'Ayy Lmao', 
            'desc': 'a demo webm', 
            }
  headers = {'content-type': 'application/json'}

  r = requests.post("http://127.0.0.1:8000/webms/api/", 
      auth=(user,password),
      data=json.dumps(payload),headers=headers)

  print r.json

if __name__ == "__main__":
  main()
