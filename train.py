import sys

lines =  sys.stdin.readlines()
tag_count = {}
words = {}
words_of_word = {}
total = 0
for line in lines:
	if '\t' not in line:
		continue
	row = line.split('\t')
	tag = row[3]
	if tag == '_':
		continue
	if tag not in tag_count:
		tag_count[tag] = 0
	tag_count[tag] = tag_count[tag] + 1
	word = row[1]
	if word == '_':
		continue
	if word not in words_of_word:
		words_of_word[word] = 0
	words_of_word[word] = words_of_word[word] + 1
	if word not in words[word]:
		words[word] = {}
	if tag not in words[word]:
		words[word][tag] = 0
	words[word][tag] = words[word][tag] + 1
	total = total + 1
print()

for tag in tag_count:
	freq = tag_count[tag]/total
	print(tag, tag_count[tag], freq)

for word in words:
	for tag in words[word]:
		freq = words[word][tag]/words_of_word[word]
		print('%.2f\t%d\t%s\t%s' % (freq, words[word][tag], tag, word))
