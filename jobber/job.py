import os
import re
import requests

from bs4 import BeautifulSoup

def readfile(path):
    with open(path) as file:
        return file.read()

def readhttp(url):
    r = requests.get(url)
    if r.status_code != 200: return false
    return r.content

class Job:
    def __init__(self, fd):
        if os.path.exists(fd):
            self.html = readfile(fd)
        else:
            self.html = readhttp(fd)
        self.makesoup()

    def makesoup(self, html=None):
        if html:
            self.html = html
        if self.html:
            self.soup = BeautifulSoup(self.html, 'html.parser')
            for tag in self.soup.find_all('script'):
                tag.decompose()
