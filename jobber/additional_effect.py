import re

from bs4 import BeautifulSoup

from .guardian_effect import GuardianEffect

class AdditionalEffect(GuardianEffect):
    def __init__(self, text):
        super().__init__('additional-effect', '')
        self.root = self.soup.find(name='additional-effect')
        if text[:19] == 'Additional Effect: ':
            self.root.string = text[19:]
        else:
            x, y = re.search(r'\w++ Effect:', text).span()
            self.set_name(text[:y-8])
            self.set_description(text[y+1:])

    def set_name(self, text):
        name = self.soup.new_tag('name')
        name.string = text
        self.root.append(name)

    def set_description(self, text):
        description = self.soup.new_tag('description')
        description.string = text
        self.root.append(description)
