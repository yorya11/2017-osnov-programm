import sys

lines = sys.stdin.readlines()

dict = str.maketrans("абцчдэфгхийклмнопрсшзжтувюäöАБЧДЭФГХИЙКЛМНОПРСШЗЖТУВЮÄÖ","abcčdefghijklmnoprsšzžtuvyäöABČDEFGHIJKLMNOPRSŠZŽTUVYÄÖ")	
for line in lines:
	
	line = line.strip()
	if line.count('<p>') > 0:
		line = line.replace('<p>',' ').replace('</p>',' ')
		line = line.split(',')
		#print(line[0:2])
		for l in line[0:2]:
			l = l.translate(dict)
			print(''.join(l))
			