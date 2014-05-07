# !/usr/bin/env python

import json

def parse_json(content):
     return json.loads(content.decode(encoding="UTF-8"))
