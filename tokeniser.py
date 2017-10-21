import sys

lines = sys.stdin.readlines()

index = 1

for line in lines:
	if line.strip() == '':
		continue
	print('# sent_id = %d' % (index))
	print ('# line = %s' % (line.strip()))
	line = line.replace(',', ' ,').replace('.', ' .').replace('!', ' !').replace('?', ' ?').replace('(', ' (').replace(')', ' )').replace('-', ' -').replace(':', ' :')
	index = index + 1
	tokens = line.strip().split(' ')
	heh = 1
	for t in tokens:
		print(str(heh)+ '\t'+ t+ '\t_\t_\t_\t_\t_\t_\t_\t_')
		heh = heh + 1
