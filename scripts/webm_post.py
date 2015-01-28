#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import argparse

#import urllib


def main():
  parser = argparse.ArgumentParser(description='Exercise bing translation api.')
  parser.add_argument('user', help='username.', type=str)
  parser.add_argument('password', help='password.', type=str)
  parser.add_argument('url', help='url of webm.', type=str)
  args = parser.parse_args()

  url = args.url
  user = args.user
  password = args.password

  payload = {
            'channel': '#/jp/shows', 
            'nick': 'on_three', 
            'url': url,  
            }
  headers = {'content-type': 'application/json'}
  
  r = requests.post("http://127.0.0.1/webms/new/", 
    auth=(user,password),
    data=json.dumps(payload),headers=headers)

  print r.json

if __name__ == "__main__":
  main()
