import re

from bs4 import BeautifulSoup

from .granted_effect import GrantedEffect
from .guardian_effect import GuardianEffect

class GuardianCombo():
    def __init__(self):
        self.soup = BeautifulSoup('<combination></combination>', 'html.parser')

    def combo_action(self, text):
        action = GuardianEffect('combo-action', text)
        self.soup.combination.append(action.soup)

    def combo_bonus(self, text):
        bonus = GrantedEffect('combo-bonus', text)
        self.soup.combination.append(bonus.soup)

    def combo_potency(self, text):
        self.soup.combination.find_all(name='combo-action')[-1]['potency'] = text

    def cure_potency(self, text):
        self.soup.combination.contents[-1]['cure'] = text
