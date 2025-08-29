import re

from bs4 import BeautifulSoup
from .guardian_combo import GuardianCombo
from .guardian_effect import GuardianEffect

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

    def cure_potency(self, text):
        tag = self.soup.new_tag('cure-potency')
        tag.string = text
        return tag

    def deal_damage(self, text):
        self.primary = self.soup.new_tag('deal-damage')
        aspect = re.search(r'Deals \w+ damage', text).group()[6:-7]
        potency = re.search(r'with a potency of \d+', text).group()
        potency = re.search(r'\d+', potency).group()
        self.primary['aspect'] = aspect
        self.primary['potency'] = potency
        if 'to all nearby enemies' in text:
            self.primary['area'] = 'circle'
        elif 'to all enemies in a straight line before you' in text:
            self.primary['area'] = 'line'
        elif 'to all enemies in a cone before you' in text:
            self.primary['area'] = 'cone'
        self.primary.string = text

    def deliver_attack(self, text):
        self.primary = self.soup.new_tag('deliver-attack')
        if len(re.findall(r'\d+', text)) > 0:
            potency = int(re.findall(r'\d+', text)[0])
        else:
            potency = 0
        self.primary['potency'] = potency
        self.primary.string = text

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
        tag.string = text
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
        for line in lines:
            soup = BeautifulSoup(line, 'html.parser')
            text = soup.text.strip()
            if text == '': continue
            if text[:1] == '※':
                tag = self.bullet(text[1:])
                table_of_contents.append(tag)
            elif text[:19] == 'Additional Effect: ':
                tag = self.additional_effect(text[19:])
                table_of_contents.append(tag)
            elif text[:14] == 'Combo Action: ':
                self.combination = GuardianCombo()
                self.combination.combo_action(text[14:])
                table_of_contents.append(self.combination.soup)
            elif text[:13] == 'Combo Bonus: ':
                self.combination.combo_bonus(text[13:])
            elif text[:15] == 'Combo Potency: ':
                self.combination.combo_potency(text[15:])
            elif text[:14] == 'Cure Potency: ':
                if hasattr(self, 'combination'):
                    self.combination.cure_potency(text[14:])
                else:
                    self.cure_potency(text[14:])
            elif re.search(r'Deals \w+ damage', text):
                self.deal_damage(text)
                table_of_contents.append(self.primary)
            elif text[:8] == 'Delivers':
                self.deliver_attack(text)
                table_of_contents.append(self.primary)
            elif text[:10] == 'Duration: ':
                table_of_contents[-1]['duration'] = self.duration(text)
            elif text[:7] == 'Extends':
                tag = self.extend_duration(text)
                table_of_contents.append(tag)
            elif text[:9] == 'Potency: ':
                tag = table_of_contents[-1]
                tag['potency'] = self.potency(text)
            elif text[:21] == 'Shares a recast timer':
                tag = self.share_recast(text)
                table_of_contents.append(tag)
            else:
                tag = self.primary_effect(text)
                table_of_contents.append(tag)
        return table_of_contents
