import re

from bs4 import BeautifulSoup

from .effect import Effect

class GuardianEffect(Effect):
    def __init__(self, name, text):
        super().__init__(name)
        self.root = self.soup.find(name=name)
        self.root.string = text

    def set_cure_potency(self, text):
        self.root['cure-potency'] = self.parse_integer(text)

    def set_description(self, text):
        self.root.string = text
        if 'with a potency of' in text:
            potency = re.search(r'with a potency of [0-9,]+', text)
            potency = potency.group()[18:]
            self.root['potency'] = potency
        if 'to all nearby enemies' in text:
            self.root['area'] = 'circle'
            self.root['target'] = 'nearby enemies'
        elif 'in a straight line before you' in text:
            self.root['area'] = 'line before'
        elif 'in a cone before you' in text:
            self.root['area'] = 'cone before'
        elif 'in a cone behind you' in text:
            self.root['area'] = 'cone behind'
        elif 'to target and all enemies nearby it' in text:
            self.root['area'] = 'target circle'
            self.root['target'] = 'target nearby enemies'

    def set_duration(self, text):
        self.root['duration'] = self.milliseconds(text)

    def set_maximum_charges(self, text):
        self.root['maximum-charges'] = self.parse_integer(text)

    def set_potency(self, text):
        self.root['potency'] = self.parse_integer(text)
