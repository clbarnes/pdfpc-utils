#!/usr/bin/env python3

import sys

path, added_slide = sys.argv[1], sys.argv[2]
added_slide = int(added_slide)

with open(path,'r') as f:
	text = f.read()

lines = text.split('\n')

for i, line in enumerate(lines):
	if line.startswith('### '):
		slide_no = int(line[4:])
	else:
		continue
	
	if slide_no == added_slide:
		insert_at = i
	if slide_no >= added_slide:
		lines[i] = '### {}'.format(slide_no+1)

lines.insert(insert_at, '### {}'.format(added_slide))

with open(path,'w') as f:
	f.write('\n'.join(lines))

print('Inserted slide number {} at line {}'.format(str(added_slide), insert_at))
