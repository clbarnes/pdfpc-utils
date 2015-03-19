#!/usr/bin/env python3

import re
import sys

tex_path = sys.argv[1]
out_path = sys.argv[2]

frame_re = re.compile(r'\\begin\{frame\}(.*?)\\end\{frame\}', re.DOTALL)
note_re = re.compile(r'\\note\{(.*?)\}', re.DOTALL)

lines = ['[file]', tex_path[0:-4] + '.pdf', '[notes]']

with open(tex_path, 'r') as tex_file:
	text = tex_file.read()

for frame_no, frame_text in enumerate(re.findall(frame_re, text)):
	lines.append('### {}'.format(frame_no+1))
	notes = note_re.findall(frame_text)
	lines.extend(notes)
			
with open(out_path, 'w') as out_file:
	out_file.write('\n'.join(lines))
