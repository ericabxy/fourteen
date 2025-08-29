import re

from bs4 import BeautifulSoup
from .guardian_content import GuardianContent

class AdditionalEffect(GuardianContent):
    def __init__(self):
        self.soup = BeautifulSoup('<html>Soup</html>', 'html.parser')
        self.root = self.soup.new_tag('additional-effect')

    def add_description(self, text):
        effect = self.soup.new_tag('description')
        if text[:7] == 'Grants ':
            effect.name = 'granted-effect'
            x = text.find('to target', 7)
            if x > 0:
                effect['totarget'] = 'true'
                effect.string = text[7:x]
            else:
                effect.string = text[7:]
        elif text[:10] == 'Increases ':
            effect.name = 'increase-effect'
            effect.string = text[10:]
        else:
            effect.string = text
        self.root.append(effect)

    def add_duration(self, text):
        pass

    def add_potency(self, text):
        if text.find('Potency: ') >= 0:
            x = content.find('Potency: ')
            if len(re.findall(r'\d+', content)) > 0:
                effect['potency'] = int(re.findall(r'\d+', content)[0])
            else:
                effect['potency'] = 0
