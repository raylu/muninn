#!/usr/bin/env python3

import os
import re
import string

emph_re = re.compile(r'\/\b(.+)\b\/')

with open('story', 'r') as f:
	raw = f.read()

content = ''
title, *chapters = raw.split('\n\n--\n\n')
for i, chapter in enumerate(chapters):
	chapter = emph_re.sub(r'\\emph{\1}', chapter)
	chapter = chapter.replace(' - ', ' -- ')
	chapter = chapter.replace('...', '\\ldots ')
	content += '\chapter{}\n\n' + chapter
content += '\n'
for _ in range(82):
	content += '\n\\newpage\\null'

with open('format.tex', 'r') as infile, open('story.tex', 'w') as outfile:
	t = string.Template(infile.read())
	outfile.write(t.substitute(title=title, content=content))

os.execvp('pdflatex', ['pdflatex', 'story.tex'])
