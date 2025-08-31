import re

from bs4 import BeautifulSoup

from .additional_effect import AdditionalEffect
from .combo_action import ComboAction
from .combo_bonus import ComboBonus
from .guardian_effect import GuardianEffect
from .named_cost import NamedCost
from .named_effect import NamedEffect
from .primary_effect import PrimaryEffect

class GuardianContent:
    def __init__(self, tag):
        self.soup = BeautifulSoup('<></>', 'html.parser')
        self.src = tag

    def additional_effect(self, text):
        tag = self.soup.new_tag('additional-effect')
        tag.string = text
        return tag

    def bullet(self, text):
        tag = self.soup.new_tag('bullet-point')
        tag.string = text
        return tag

    def duration(self, text):
        if len(re.findall(r'\d+', text)) > 1:
            return int(float(re.findall(r'\d+\.\d+', text)[0]) * 1000)
        elif len(re.findall(r'\d+', text)) > 0:
            return int(re.findall(r'\d+', text)[0]) * 1000
        else:
            return 0

    def extend_duration(self, text):
        tag = self.soup.new_tag('extend-duration')
        effect = re.search(r'Extends \w++ duration', text).group()[8:-9]
        by = re.search(r'duration by \d+s', text).group()[12:-1]
        maximum = re.search(r'to a maximum of \d+s', text).group()[16:-1]
        tag['extend'] = int(by) * 1000
        tag['maximum'] = int(maximum) * 1000
        tag.string = effect 
        return tag

    def granted_effect(self, text):
        tag = self.soup.new_tag('granted-effect')
        x, y = re.search(r'\w++ Effect: ', text).span()
        tag.append(self.soup.new_tag( 'named' ))
        tag.named.string = text[:y-9]
        tag.append(self.soup.new_tag( 'description' ))
        tag.description.string = text[y:]
        return tag
    
    def potency(self, text):
        return re.search(r'\d+', text).group()

    def primary_effect(self, text):
        x = text.find('Gauge Cost: ')
        if x > 0:
            tag = self.soup.new_tag('job-gauge')
            name = text[:x+5]
            tag['cost'] = text[x+12:]
            tag.string = name
        else:
            tag = self.soup.new_tag('primary-effect')
            tag.string = text
            self.primary = tag
        return tag

    def share_recast(self, text):
        tag = self.soup.new_tag('share-recast')
        tag.string = text
        return tag

    def table_of_contents(self):
        table_of_contents = []
        lines = str(self.src.find_all(class_='content')[0]).split('<br/>')
        current_effect = PrimaryEffect()
        for line in lines:
            soup = BeautifulSoup(line, 'html.parser')
            text = soup.text.strip()
            if text == '': continue
            if text[:1] == '※':
                tag = self.bullet(text[1:])
                table_of_contents.append(tag)
            elif text[:19] == 'Additional Effect: ':
                current_effect = AdditionalEffect(text[19:])
                table_of_contents.append(current_effect.soup)
            elif re.search(r'\w++ Effect:', text):
                current_effect = NamedEffect(text)
                table_of_contents.append(current_effect.soup)
            elif re.search(r'\w++ Gauge Cost:', text):
                current_effect = NamedCost(text)
                table_of_contents.append(current_effect.soup)
            elif text[:14] == 'Combo Action: ':
                current_effect = ComboAction(text[14:])
                table_of_contents.append(current_effect.soup)
            elif text[:13] == 'Combo Bonus: ':
                current_effect = ComboBonus(text[13:])
                table_of_contents.append(current_effect.soup)
            elif text[:15] == 'Combo Potency: ':
                current_effect.set_potency(text[15:])
            elif text[:14] == 'Cure Potency: ':
                current_effect.set_cure_potency(text[14:])
            elif re.search(r'Deals \w+ damage', text):
                current_effect.deal_damage(text)
                table_of_contents.append(current_effect.soup)
            elif text[:8] == 'Delivers':
                current_effect.deliver_attack(text)
                table_of_contents.append(current_effect.soup)
            elif text[:10] == 'Duration: ':
                current_effect.set_duration(text[10:])
            elif re.search(r'Extends \w++ duration', text):
                tag = self.extend_duration(text)
                table_of_contents.append(tag)
            elif text[:17] == 'Maximum Charges: ':
                current_effect.set_maximum_charges(text)
            elif text[:9] == 'Potency: ':
                current_effect.set_potency(text)
            elif text[:21] == 'Shares a recast timer':
                tag = self.share_recast(text)
                table_of_contents.append(tag)
            else:
                current_effect = PrimaryEffect()
                current_effect.set_description(text)
                table_of_contents.append(current_effect.soup)
        return table_of_contents
