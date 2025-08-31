import re

from bs4 import BeautifulSoup

from .guardian_effect import GuardianEffect

class NamedEffect(GuardianEffect):
    def __init__(self, text):
        super().__init__('named-effect', '')
        self.root = self.soup.find(name='named-effect')
        x, y = re.search(r'\w++ Effect: ', text).span()
        self.set_name(text[ :y-9 ])
        self.set_description(text[ y: ])

    def set_name(self, text):
        name = self.soup.new_tag('name')
        name.string = text
        self.root.append(name)

    def set_description(self, text):
        description = self.soup.new_tag('description')
        description.string = text
        self.root.append(description)
