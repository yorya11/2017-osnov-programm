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
<<<<<<< HEAD
		heh = heh + 1
=======
		heh = heh + 1
>>>>>>> f4ff14d72685ea07e6a12a0f429a443cff815942
