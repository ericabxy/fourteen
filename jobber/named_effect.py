import re

from bs4 import BeautifulSoup

from .effect import Effect

class NamedEffect(Effect):
    def __init__(self, text):
        super().__init__('named-effect')
        self.root = self.soup.find(name='named-effect')
        x, y = re.search(r'\w++ Effect: ', text).span()
        self.root.string = text  #[:y-9]
