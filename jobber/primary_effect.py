import re

from bs4 import BeautifulSoup
from .effect import Effect

class PrimaryEffect(Effect):
    def __init__(self):
        super().__init__('primary-effect')
        self.root = self.soup.find(name='primary-effect')

    def deal_damage(self, text):
        self.root.name = 'deal-damage'
        aspect = re.search(r'Deals \w+ damage', text).group()[6:-7]
        potency = re.search(r'with a potency of \d+', text).group()
        potency = re.search(r'\d+', potency).group()
        self.root['aspect'] = aspect
        self.root['potency'] = potency
        if 'to all nearby enemies' in text:
            self.root['area'] = 'circle'
        elif 'to all enemies in a straight line before you' in text:
            self.root['area'] = 'line'
        elif 'to all enemies in a cone before you' in text:
            self.root['area'] = 'cone'
        self.root.string = text

    def deliver_attack(self, text):
        self.root.name = 'deliver-attack'
        if len(re.findall(r'\d+', text)) > 0:
            potency = int(re.findall(r'\d+', text)[0])
        else:
            potency = 0
        self.root['potency'] = potency
        self.root.string = text
