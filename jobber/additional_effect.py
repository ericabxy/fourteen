import re

from bs4 import BeautifulSoup

from .effect import Effect

class AdditionalEffect(Effect):
    def __init__(self, text):
        super().__init__('additional-effect')
        self.root = self.soup.find(name='additional-effect')
        self.root.string = text
