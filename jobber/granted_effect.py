import re

from bs4 import BeautifulSoup

from .guardian_effect import GuardianEffect

class GrantedEffect(GuardianEffect):
    def __init__(self, name, text):
        effect = text
        for reg in re.findall('Grants ', text):
            effect = text[7:]
        for reg in re.findall('Grants \w+,', text):
            effect = reg[7:-1]
        for reg in re.findall('Grants \w+ to target', text):
            effect = reg[7:-10]
        super().__init__(name, effect)
        self.soup.find()['grant'] = True
