import re

from bs4 import BeautifulSoup

class GuardianEffect:
    def __init__(self, name, text):
        html_doc = '<' + name + '>' + '</' + name + '>'
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.soup.find().string = text
