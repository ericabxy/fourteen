import re

from bs4 import BeautifulSoup

from .guardian_effect import GuardianEffect

class ComboBonus(GuardianEffect):
    def __init__(self, text):
        super().__init__('combo-bonus', '')
        self.root = self.soup.find(name='combo-bonus')
        self.root.string = text
