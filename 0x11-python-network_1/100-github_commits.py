#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve a challenge. """

import sys
import requests

if __name__ == "__main__":
    url = ("https://developer.github.com/v3/repos/commits".format(sys.argv[2], sys.argv[1]))
    r = requests.get(url)
    commit = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
