import string 
from math import log
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
with open ("cran/cran.all.1400", "r") as myfile:
	data = myfile.read().replace('\n', ' ')
#print(data)
#data = data.lower()

docs = data.split(".I")
#print(docs[10])
doc_body = [""]
for doc in docs[1:]:
	doc_body.append(doc.split(".W")[1])

#print(len(doc_body))
wordlist=[[]]
for doc in doc_body:
	doc = doc.lower()
	for c in string.punctuation:
		doc = doc.replace(c,"")
	words=doc.split(" ")
	words=[w for w in words if w not in stop]	#stopword removal
	wordlist.append(words)
for words in wordlist:
	words=[word for word in words if word!='']	
#print(len(wordlist))



myset = set()
for doc in wordlist:
	myset = myset.union(set(doc))
myset.discard('')
#print(myset)
mydict = {}
for w in myset:
	mydict[w] = []
	for doc in wordlist:
		if w in doc:
			mydict[w].append((wordlist.index(doc),doc.count(w)))



#print(mydict)#print(mydict)

def cosineScore(q):
	N = len(wordlist)
	scores = [[i,0] for i in range(N)]
	length = [len(w) for w in wordlist]
	#print(length)
	q = q.lower()
	for c in string.punctuation:
		q = q.replace(c,"")
	qu = q.strip().split(" ")
	qu=[w for w in qu if w not in stop]
	for term in qu:
		post  = mydict[term]
		#print(post)
		idf = log(N / len(post))
		tq = qu.count(term)
		for p in post:
			wf = 1 + log(p[1]) 
			scores[p[0]][1] +=  wf * idf * tq

		for d in range(1,N):
			scores[d][1] /= length[d]
	scores.sort(key=lambda kv: kv[1], reverse=True)
	#print(scores[:11])
	for i in scores[:11]:
		print(i[0], end=",")
	print()
#query=input()
#query="experimental"

query = "can increasing the edge loading of a plate beyond the critical value for buckling change the buckling mode"
cosineScore(query)

#cosineScore("properties of impact pressure probes in free molecule flow")
