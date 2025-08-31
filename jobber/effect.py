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

    def number(self, text):
        if len(re.findall(r'\d+', text)) > 0:
            return int(re.findall(r'\d+', text)[0])
        else:
            return 0

    # TODO: put these in subclass
    def set_cure_potency(self, text):
        self.root['cure-potency'] = self.number(text)

    def set_description(self, text):
        self.root.string = text

    def set_duration(self, text):
        self.root['duration'] = self.milliseconds(text)

    def set_maximum_charges(self, text):
        self.root['maximum-charges'] = self.number(text)

    def set_potency(self, text):
        self.root['potency'] = self.number(text)
