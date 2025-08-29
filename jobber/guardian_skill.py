import re

from bs4 import BeautifulSoup
from .guardian_content import GuardianContent
from .skill import Skill

class GuardianSkill(Skill):
    def __init__(self, tag):
        super().__init__(tag)

    def action_name(self):
        skill = super().text('skill')
        if 'Class Quest' in skill:
            skill = skill[:-11].strip()
        elif 'Job Quest' in skill:
            skill = skill[:-9].strip()
        elif 'Prerequisite Quest' in skill:
            skill = skill[:-18].strip()
        return skill

    def classification(self):
        return super().text('classification')

    def description(self):
        desc = GuardianContent(self.src)
        return desc.table_of_contents()

    def distance_and_range(self):
        text = super().text('distant_range')
        range_s = text.split()[0]
        radius_s = text.split()[1]
        range_n = int(re.findall(r'\d+', range_s)[0])# * 36
        radius_n = int(re.findall(r'\d+', radius_s)[0])# * 36
        return range_n, radius_n

    def level_acquired(self):
        return super().number('jobclass')

    def mp_cost(self):
        return super().number('cost')

    def time_to_cast(self):
        return super().milliseconds('cast')

    def time_to_recast(self):
        return super().milliseconds('recast')
