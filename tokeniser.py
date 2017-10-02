import sys

lines = sys.stdin.readlines()

index = 1

for line in lines:
	print('# sent_id = %d' % (index))
	print ('# line = %s' % (line))
	line = line.replace(',', ' ,').replace('.', ' .').replace('!', ' !').replace('?', ' ?').replace('(', ' (').replace(')', ' )').replace('-', ' -').replace(':', ' :')
	index = index + 1
	tokens = line.split(' ')
	heh = 1
	for t in tokens:
		print(heh, '\t', t, '\t', '_', '\t', '_', '\t', '_', '\t', '_', '\t', '_', '\t', '_','\t', '_','\t', '_')
		heh = heh + 1