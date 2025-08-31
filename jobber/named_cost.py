import re

from bs4 import BeautifulSoup

from .effect import Effect

class NamedCost(Effect):
    def __init__(self, text):
        super().__init__('named-cost')
        self.root = self.soup.find(name='named-cost')
        x, y = re.search(r'\w++ Cost: ', text).span()
        self.root.string = text[:y-7]
        self.root['cost'] = self.parse_integer(text[y:])
