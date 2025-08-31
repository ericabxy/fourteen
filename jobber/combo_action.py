import re

from bs4 import BeautifulSoup
from .guardian_effect import GuardianEffect

class ComboAction(GuardianEffect):
    def __init__(self, text):
        super().__init__('combo-action', '')
        self.root = self.soup.find(name='combo-action')
        self.root.string = text

    def set_cure_potency(self, text):
        self.root['cure_potency'] = self.number(text)

    def set_duration(self, text):
        self.root['duration'] = self.milliseconds(text)

    def set_potency(self, text):
        self.root['potency'] = self.parse_integer(text)
