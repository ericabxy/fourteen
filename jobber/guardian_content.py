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
        if re.match('^Grants ', text):
            tag.append(self.grants( text ))
        else:
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
        affinity = re.search(r'Deals \w+ damage', text).group()[6:-7]
        potency = re.search(r'with a potency of \d+', text).group()
        potency = re.search(r'\d+', potency).group()
        self.primary['affinity'] = affinity
        self.primary['potency'] = potency

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
            n = int(float(re.findall(r'\d+\.\d+', text)[0]) * 1000)
        elif len(re.findall(r'\d+', text)) > 0:
            n = int(re.findall(r'\d+', text)[0]) * 1000
        else:
            n = 0
        self.primary['duration'] = n

    def granted_effect(self, text):
        tag = self.soup.new_tag('granted-effect')
        tag.string = text
        return tag

    def grants(self, text):
        tag = self.soup.new_tag('grant')
        grant = text[7:]
        for reg in re.findall('Grants \w+,', text):
            grant = reg[7:-1]
        for reg in re.findall('Grants \w+ to target', text):
            grant = reg[7:-10]
        tag.string = grant
        return tag

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
                self.duration(text)
            else:
                tag = self.primary_effect(text)
                table_of_contents.append(tag)
        return table_of_contents
