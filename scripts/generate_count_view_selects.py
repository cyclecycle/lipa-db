import os
from itertools import takewhile

view_select_dir = 'sql/views/select'
view_select_count_dir = 'sql/views/select/count'
view_select_files = os.scandir(view_select_dir)
for view_select_file in view_select_files:
    if os.path.isdir(view_select_file):
        continue
    with open(view_select_file) as f:
        content = f.read()
    lines = content.splitlines()
    select_line = lines[0]
    lines_until_from = list(takewhile(lambda l: l != 'from', lines))
    from_line_idx = len(lines_until_from)
    line_to_count = lines_until_from[1]
    line_to_count = line_to_count.strip().replace(',', '')
    count_line = '    count({})'.format(line_to_count)
    lines = [select_line, count_line] + lines[from_line_idx:len(lines)]
    content = '\n'.join(lines)
    new_file_name = view_select_file.name.replace('select', 'select_count')
    new_file_path = os.path.join(view_select_count_dir, new_file_name)
    with open(new_file_path, 'w') as f:
        f.write(content)
