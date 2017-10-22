import sys

frequent_tag = 'x'
count = 0
fd = open('model.tsv')

for line in fd.readlines():
	line = line.strip('\n')
	line = line.split('\t')
	if int(line[1]) > count:
		count = int(line[1])
		frequent_tag = line[2]
print(frequent_tag)
input = sys.stdin.readlines()
for line in input:
	line = line.strip()
	if '\t' not in line:
		continue 
	row = line.split('\t')
	row[3] = frequent_tag
	print('\t', join(row))
