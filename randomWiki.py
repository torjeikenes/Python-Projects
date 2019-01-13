#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 torje <torje@torje-laptop>
#
# Distributed under terms of the MIT license.

"""

"""

from urllib.request import urlopen
import json
import webbrowser
import subprocess

url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&format=json"


while True:
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    title = data["query"]["random"][0]["title"]
    wikiId = data["query"]["random"][0]["id"]


    print("Do you want to read about: " + title + "?  [Y/n]")
    answer = input()

    if answer == "" or answer.lower() == "y":
        #webbrowser.open("http://en.wikipedia.org/wiki?curid="+str(wikiId))
        r = subprocess.getoutput("google-chrome-stable http://en.wikipedia.org/wiki?curid="+str(wikiId))
        r
        input("Press [Enter] to get a new page")
    elif answer.lower() == "n":
        print("Ok. Here is a new page:")
    else:
        print("please write y or n")

