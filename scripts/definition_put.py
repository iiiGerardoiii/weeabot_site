#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

payload = {'channel': '#/jp/shows', 'nick': 'swam', 'url':'www.jisho.org', 'text':'doko','word':'どこ'}
headers = {'content-type': 'application/json'}
r = requests.post("http://127.0.0.1:8000/jisho/api/", data=json.dumps(payload), headers=headers)
