import sys

lines = sys.stdin.readlines()

sent_id = 1
dict = str.maketrans("abčdefghijklmnoprsšzžtuvyäöABČDEFGHIJKLMNOPRSŠZŽTUVYÄÖ", "абчдэфгхийклмнопрсшзжтувюäöАБЧДЭФГХИЙКЛМНОПРСШЗЖТУВЮÄÖ")

for c in lines:
	number = 1
	c = c.replace('.', ' .').replace(',', ' ,').replace(':', ' :').replace(';', ' ;').replace('?', ' ?').replace('!', ' !')
	c = c.split(' ')
	print(sent_id)
	for a in c:
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\ttranslit=%s'%(number,a,a.translate(dict)))
		number=number+1
	sent_id=sent_id+1