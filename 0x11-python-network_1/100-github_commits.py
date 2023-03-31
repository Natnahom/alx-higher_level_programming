#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve a challenge. """

import sys
import requests
from request.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = request.get("https://developer.github.com/v3/repos/commits", auth=auth)
    print(r.json().get("repository-name"))
    print(r.json().get("name"))
