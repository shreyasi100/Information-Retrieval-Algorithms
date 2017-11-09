from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import *
stop = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
fp = open("TIME.ALL","r")
#fp = open("testfile","r")
op = open("OutputLog","w")
contents=fp.read()
contents=contents.lower()
rawlist=contents.split(" ")
rawset = set(rawlist)
print("Raw set: ", len(rawset))
op.write("Size of vocabulary before processing: "+str(len(rawset))+"\n")
wordlist = tokenizer.tokenize(contents)
'''--------Stopword Removal------'''
wordlist=[w for w in wordlist if w not in stop]
op.write("Vocabulary --- After stopword removal,Before stemming:\n")
op.write(str(set(wordlist)))
op.write("\n")
stemmer = PorterStemmer()
'''--------Stemming------'''
stemmedlist =  [stemmer.stem(word) for word in wordlist]
stemmedset=set(stemmedlist)
op.write("Vocabulary --- After stemming:\n")
op.write(str(stemmedset))

print("Stemmed set: ",len(stemmedset))
op.write("Size of vocabulary after processing: "+str(len(stemmedset)))
