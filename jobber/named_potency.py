import re

from bs4 import BeautifulSoup

from .guardian_effect import GuardianEffect

class NamedPotency(GuardianEffect):
    def __init__(self, text):
        super().__init__('named-potency', '')
        self.root = self.soup.find(name='named-potency')
        x, y = re.search(r'\w++ Potency: ', text).span()
        self.root.string = text[:y-10]
        self.root['potency'] = self.parse_integer(text[y:])
