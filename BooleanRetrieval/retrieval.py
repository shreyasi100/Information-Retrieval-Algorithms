import string
import time
start_time = time.time()
with open ("wiki.csv", "r") as myfile:
	data = myfile.read()
#print(data)
lines = data.split("\n")
#print(lines)
docId = 0
myDict = {}
for line in lines:
	sen = line.split("\t")
	#print(sen)
	if(len(sen) == 2):
		data = sen[1]
		data = data.lower()
		for c in string.punctuation:
			data= data.replace(c,"")
		words = data.split(" ")
		#print(words)
		for word in words:
			if word in myDict:
				myDict[word].append(docId)
			else:
				myDict[word] = [docId]
	docId +=1
#print(myDict)
				
def search_and(word1, word2):
	
	list_a = myDict[word1]
	list_b = myDict[word2]
	
	#print(list_a)
	#print(list_b)	
	inter = []
	for i in list_a:
		if i in list_b:
			#print(i)
			inter.append(i)
	return inter
#search_and("is", "he")

def displayRes(word1, word2, k):
	inter = search_and(word1, word2)
	len_inter = len(inter)
	if(len_inter > k):
		inter = inter[:k]
	#len_inter = len(inter)
	for i in inter:
		print(lines[i])

#displayRes("is", "he")
def displayDocId(word1, word2):
	res = search_and(word1, word2)
	for i in res:
		print(i)


n = int(input("Enter 1 for getting document ID and 2 for geting document contents: "))
if(n == 1):
	w1 = input("Enter the first word: ")
	w2 = input("Enter the second word: ")
	displayDocId(w1, w2)
else: 
	w1 = input("Enter the first word: ")
	w2 = input("Enter the second word: ")
	k = int(input("Enter the value of k: "))
	displayRes(w1, w2, k)	
print("---Result displayed in %s seconds ---" % (time.time() - start_time))
