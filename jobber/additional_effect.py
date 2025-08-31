import re

from bs4 import BeautifulSoup

from .guardian_effect import GuardianEffect

class AdditionalEffect(GuardianEffect):
    def __init__(self, text):
        super().__init__('additional-effect', '')
        self.root = self.soup.find(name='additional-effect')
        self.root.string = text
