#story_id,story_time,story_url,story_text,story_author,comment_id,comment_text,comment_author,comment_ranking,author_comment_count,story_comment_count

import csv
import codecs
import sys

unigrams = {}
skipgrams = {}


def P(text,tokens):
	p = float(tokens[text]) / float(len(tokens))
	if p == 0.0:
		p = sys.float_info.min
	return p

def skipgramP(skipgram,skigrams,unigrams):
	p0 = P(skipgram[0],unigrams)
	p1 = P(skipgram[1],unigrams)
	sP = P(skipgram,skigrams)

	print p0,p1,sP

	return (sP/p0/p1)

def tokenize(text,tokens):
	text = text.replace('<p>',' ')
	words = text.split(" ")
	for word in words:
		try:
			tokens[word] += 1
		except:
			tokens[word] = 0
	return tokens

def findskipgrams(skip,text,tokens):
	text = text.replace('<p>',' ')
	words = text.split(" ")
	for i in xrange(1,len(words)-1):
		word0 = words[i-skip]
		word1 = words[i]
		word2 = words[i+skip]

		try:
			skipgrams[(word0,word1)] += 1
		except:
			skipgrams[(word0,word1)] = 0
		try:
			skipgrams[(word1,word2)] += 1
		except:
			skipgrams[(word1,word2)] = 0


	return tokens

#csvdata = csv.reader(codecs.open('hacker_news_comments.csv', 'rU', 'utf-16'))
csvdata = csv.reader(open('hacker_news_comments2.csv'))

for row in csvdata:
	story_text = row[3]
	comment_text = row[6]

	#unigrams = tokenize(story_text,unigrams)
	#skipgrams = findskipgrams(1,story_text,skipgrams)

	unigrams = tokenize(comment_text,unigrams)
	skipgrams = findskipgrams(1,comment_text,skipgrams)


print "unigrams:",len(unigrams)
print "skipgrams:",len(skipgrams)

#for unigram in unigrams:
#	print unigram,P(unigram,unigrams)


for skipgram in skipgrams:
	print skipgram,skipgramP(skipgram,skipgrams,unigrams)
