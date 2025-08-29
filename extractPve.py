import re
import sys

from bs4 import BeautifulSoup
from jobber import Character

with open(sys.argv[1]) as file:
    html_doc = file.read()
    new_character = Character(html_doc)
    new_character.set_skills_from_id()
    print('<?xml-stylesheet type="text/xml" href="default.xslt"?>')
    print(new_character.root.prettify( ))
