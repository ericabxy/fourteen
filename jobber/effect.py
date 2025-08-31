import re

from bs4 import BeautifulSoup

class Effect:
    def __init__(self, name):
        html_doc = '<' + name + '>' + '</' + name + '>'
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def milliseconds(self, text):
        if len(re.findall(r'\d+', text)) > 1:
            n = int(float(re.findall(r'\d+\.\d+', text)[0]) * 1000)
        elif len(re.findall(r'\d+', text)) > 0:
            n = int(re.findall(r'\d+', text)[0]) * 1000
        else:
            n = 0
        return n

    def parse_integer(self, text):
        match0 = re.search(r'[0-9,]+', text)
        if match0:
            number = match0.group().replace(',', '')
            return int(number)
