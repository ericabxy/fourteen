import re

from bs4 import BeautifulSoup
from .guardian_effect import GuardianEffect

class PrimaryEffect(GuardianEffect):
    def __init__(self):
        super().__init__('primary-effect', '')
        self.root = self.soup.find(name='primary-effect')

    def deal_damage(self, text):
        aspect = re.search(r'Deals \w+ damage', text).group()[6:-7]
        potency = re.search(r'with a potency of \d+', text).group()
        potency = re.search(r'\d+', potency).group()
        self.root['damage'] = aspect
        self.root['potency'] = potency
        self.set_description(text)

    def deliver_attack(self, text):
        attack = re.search(r'Delivers (a|an) \w+ attack', text)
        potency = re.search(r'with a potency of \d+', text)
        if re.search(r'Delivers a \w+ attack', text):
            attack_type = attack.group()[11:-7]
            self.root['attack'] = attack_type
        if potency:
            self.root['potency'] = self.parse_integer(potency.group( ))
        self.set_description(text)
