#!/usr/bin/env python3
import os
import json
from templates import login_page

environment = {}
for env_key, env_value in os.environ.items():
    environment[env_key] = env_value
# print("Content-Type: application/json")
# print()
# print(json.dumps(environment))
# print(environment["QUERY_STRING"] + environment["HTTP_USER_AGENT"])
print("Content-Type: text/html\r\n")
print(login_page())