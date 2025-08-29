import re

from bs4 import BeautifulSoup
from .guardian_skill import GuardianSkill

class Character:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.html = html
        self.root = BeautifulSoup('<character></character>', 'html.parser').character

    def set_skills_from_id(self, search='^pve_action'):
        for tag in self.soup.find_all(id=re.compile(search)):
            skill0 = GuardianSkill(tag)
            range_n, radius = skill0.distance_and_range()
            classification = skill0.classification()
            time_to_cast = skill0.time_to_cast()
            time_to_recast = skill0.time_to_recast()
            mpcost = skill0.mp_cost()
            action = self.soup.new_tag(classification.lower( ))
            action['level'] = skill0.level_acquired()
            if range_n > 0:
                action['range'] = range_n
            if radius > 0:
                action['radius'] = radius
            if time_to_cast > 0:
                action['cast'] = time_to_cast
            if time_to_recast > 0:
                action['recast'] = time_to_recast
            if mpcost > 0:
                action['mpcost'] = mpcost
            name = self.soup.new_tag('name')
            name.string = skill0.action_name()
            action.append(name)
            for content in skill0.description():
                action.append(content)
            self.root.append(action)
