# Mohammad Baghbanzadeh
# 9812223158

import re

with open('wiki.txt', 'r') as f:
    wikipedia_text = f.read()

patterns = [
    r'<(\/)?(math|sub|sup)>',
    r'<math>\([^<]*\)<\/math>',
    r'<math display="block">\([^<]*\)<\/math>',     # block equation should be between \[ and ]\.
    r'\[\[\(.*\)\]\]',
    r"'''.*?'''",
    r"'''(.*?)'''",
    r"''(.*?)''"
]

replacements = {
    '<math>': '$',
    '</math>': '$',
    '<sub>': '_',
    '</sub>': '',
    '<sup>': '^',
    '</sup>': '',
    "'''": '\\textbf{',
    "'''": '}',
    "''": '\\textit{',
    "''": '}',
}

for pattern in patterns:
    for tag in re.findall(pattern, wikipedia_text):
        LaTeX = ''
        if pattern == patterns[0]:
            LaTeX = replacements.get('<' + tag[1] + '>', '') if tag[0] else replacements.get('</' + tag[1] + '>', '')
        elif pattern == patterns[1]:
            LaTeX = '$$' + tag + '$$'
        elif pattern == patterns[2]:
            LaTeX = '\[' + tag + ']\\'
        elif pattern == patterns[3]:
            LaTeX = '\\textbf{' + tag.replace('[[', '').replace(']]', '') + '}'
        elif pattern == patterns[4]:
            LaTeX = '\\textbf{' + tag.replace('[[', '').replace(']]', '') + '}'
        elif pattern == patterns[5]:
            LaTeX = '\\textbf{' + tag.replace("'''", "") + '}'
        elif pattern == patterns[6]:
            LaTeX = '\\textit{' + tag.replace("''", "") + '}'
        wikipedia_text = re.sub(pattern, LaTeX, wikipedia_text)

with open('output.txt', 'w') as f:
    f.write(wikipedia_text)
