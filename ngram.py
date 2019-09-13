import re
from nltk import bigrams, trigrams, ngrams
from collections import Counter, defaultdict

def model_ready():
	file_contents = open('corpus.txt','r')
	file_contents = file_contents.read()
	words = file_contents.split(" ")
	words = [word.lower() for word in words]
	# print(words)
	# words_r = re.split(r'\W+', file_contents)
	# words_r = [word.lower() for word in words_r]
	# print(words_r)
	model = defaultdict(lambda: defaultdict(lambda: 0))

	for word in words:
		for w1, w2, w3 in ngrams(words, 3, pad_right=True, pad_left=True):
			model[(w1, w2)][w3] += 1


	for first in model:
		total_count = float(sum(model[first].values()))
		for second in model[first]:
			model[first][second] /= total_count

	# print(model['automate', 'stark’s'])
	# print(model['just', 'a'])
	return model

model_1 = model_ready()
print(dict(model_1['automate', 'stark’s']))
print(dict(model_1['sophisticated', 'artificial']))
print(dict(model_1['stark’s', 'commands']))

