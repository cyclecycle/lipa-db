import re
import os

views_template_path = 'sql/views/views_template.sql'
placeholder_pattern = re.compile(r'{{ (*)')

with open(views_template_path) as f:
    views_template = f.read()

placeholder_matches = placeholder_pattern.finditer(views_template)
for placeholder_match in placeholder_matches:
    print(placeholder_match)