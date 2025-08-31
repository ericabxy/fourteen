import re

from bs4 import BeautifulSoup

from .effect import Effect

class ComboBonus(Effect):
    def __init__(self, text):
        super().__init__('combo-bonus')
        self.root = self.soup.find(name='combo-bonus')
        self.root.string = text
