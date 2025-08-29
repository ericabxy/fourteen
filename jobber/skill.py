import re

from bs4 import BeautifulSoup

class Skill:
    def __init__(self, tag):
        self.src = tag

    def milliseconds(self, name):
        text = self.src.find_all(class_=name)[0].text.strip()
        if len(re.findall(r'\d+', text)) > 1:
            n = int(float(re.findall(r'\d+\.\d+', text)[0]) * 1000)
        elif len(re.findall(r'\d+', text)) > 0:
            n = int(re.findall(r'\d+', text)[0]) * 1000
        else:
            n = 0
        return n

    def number(self, name):
        text = self.src.find_all(class_=name)[0].text.strip()
        if len(re.findall(r'\d+', text)) > 0:
            return int(re.findall(r'\d+', text)[0])
        else:
            return 0

    def text(self, name):
        return self.src.find_all(class_=name)[0].text.strip()
