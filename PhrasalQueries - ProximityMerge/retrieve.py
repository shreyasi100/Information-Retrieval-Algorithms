#This is main program
#run: python ll2.py > results

import os
import string

class Node:

	def __init__(self, data):
		self.data = data  
		self.next = None  
 

class LinkedList:
	def __init__(self): 
		self.head = None

	

	def append(self, new_data):
		new_node = Node(new_data)
		 
		  
		if self.head is None:
			self.head = new_node
			return
		 
		last = self.head
		while (last.next):
			last = last.next
		 

		last.next =  new_node
	
	def printList(self):

		temp = self.head
		while (temp):
			print(temp.data, end="->")
			temp = temp.next
		print("NULL")

	def deleteList(self):
		self.head = None

def printDict(cdict, key):
	my_len = len(cdict[key])
	print(key)
	for k in range(0,my_len):
		mylist = cdict[key][k][1]
		print(cdict[key][k][0], end=": ")
		mylist.printList()
		print()
	#print()

'''llist = LinkedList()
llist.append(6)
llist.append(7)
llist.append(8)
a = {}
a['hello'] = (1, llist)
printDict(a, "hello")
llist.printList()
llist.deleteList()
llist.printList()
#llist.deleteList()
llist = LinkedList()
llist.append(9)
llist.append(10)
llist.append(11)
a['hi'] = (2, llist)
printDict(a, "hi")
#print("abc")'''



path = 'stories'
docId = 1
mydict = {}
stories_index = {}
for filename in os.listdir(path):
	with open(path+'/'+filename, 'r') as myfile:
		stories_index[docId] = filename
		data=myfile.read().replace('\n', ' ')
		data = data.lower()
		for c in string.punctuation:
			data= data.replace(c,"")
		myList = data.split(" ")
		#print(myList)
		len_list = len(myList)
		for i in range(0,len_list):
			#llist.append(i)
			if myList[i] in mydict:
				l = len(mydict[myList[i]])
				r = False
				for j in range(0,l):
					if(mydict[myList[i]][j][0]==docId):
						r = True
						elist = mydict[myList[i]][j][1]
						elist.append(i)
				if(r == False):
					llist = LinkedList()
					llist.append(i)
					x = (docId, llist)
					mydict[myList[i]].append(x)

			else:
				llist = LinkedList()
				llist.append(i)
				mydict[myList[i]] = [(docId, llist)]
	docId += 1
#print(mydict)
"""for key in mydict:
	printDict(mydict, key)"""
#only creating positional index
# have to still do the rest
# check if it works correctly
def print_dict():
	for key in mydict:
		printDict(mydict, key)	

#print_dict()
def search_single(word):
	for key in mydict:
		if(key == word):
			#dl = len(mydict[word])
			for i in mydict[word]:
				print(i[0], stories_index[i[0]], sep=" : ")

#serach_single("old")	
def search_and(word1, word2):
	list_a = []
	list_b = []
	for key in mydict:
		if(key == word1):
			for i in mydict[word1]:
				list_a.append(i[0])
		if(key == word2):
			for i in mydict[word2]:
				list_b.append(i[0])	
	#print(list_a)
	#print(list_b)	
	for i in list_a:
		if i in list_b:
			print(i, stories_index[i], sep=" : ")
				
#search_and("snake", "frog")


def search_or(word1, word2):
	list_a = []
	list_b = []
	for key in mydict:
		if(key == word1):
			for i in mydict[word1]:
				list_a.append(i[0])
		if(key == word2):
			for i in mydict[word2]:
				list_b.append(i[0])	
	#print(list_a)
	#print(list_b)
	list_c = set(list_a+list_b)	
	for i in list_c:
		print(i, stories_index[i], sep=" : ")


'''search_single("old")
search_and("snake", "frog")
search_or("snake", "frog")'''


def POSITIONALINTERSECT( p1, p2 , k):
	answer=list()
	t1=len(p1)
	t2=len(p2)
	#print(t1)
	#print(t2)
	m = min(t1,t2)
	i1 = 0
	i2 = 0
	while i1<t1 and i2<t2:	#until you reach end of shorter posting list
		#print("h")
		#print(p1[i1])
		#print(p2[i2])
		if p1[i1][0] == p2[i2][0]:	#docIDs equal
			l=[]
			pp1 =p1[i1][1].head #docId i1 ka posting list ka head????
			#print(pp1.data)
			pp2 =p2[i2][1].head #docId i2 ka posting list ka head????
			#print(pp2.data)
			while pp1 is not None:
				while pp2 is not None:
						if abs(pp1.data - pp2.data) <= k:
							l.append(pp2.data)
						elif pp2.data>pp1.data:
							break
						pp2=pp2.next
				while len(l)!=0 and abs(l[0]- pp1.data) > k:
					l=l[1:]
				for ps in l:
					docpos = (p1[i1][0],pp1.data,ps) #(docId,int pos of first word,int pos of second word)
					answer.append(docpos)
				pp1 = pp1.next
			i1+=1
			i2+=1
		elif p1[i1][0] < p2[i2][0]:
			i1+=1
		else:
			i2+=1
	return answer


def phrase(w1, w2, dist):
	a = []
	b = []
	for key in mydict:
		if(key == w1):
			a = mydict[key]
		if(key == w2):
			b = mydict[key]
	r = POSITIONALINTERSECT(a,b,dist)
	x = []
	for i in r:
		x.append(i[0])
	x = set(x)
	for i in x:
		print(i, stories_index[i], sep=" : ")
	
def phrase3(w1, w2, dist):
	a = []
	b = []
	for key in mydict:
		if(key == w1):
			a = mydict[key]
		if(key == w2):
			b = mydict[key]
	r = POSITIONALINTERSECT(a,b,dist)
	return r

def merge(a, b):
	l1 = len(a)
	l2 = len(b)
	l = min(l1, l2)
	res = []
	i = 0
	j = 0
	while i<l1: #optimize
		for j in range(0, l2):
			if(a[i][0] == b[j][0]):
				#print(a[i][1], b[i][1], sep = " : ")
				#print(a[i][2], b[i][2], sep = " : ")
				if(a[i][1]+1 == b[j][1] and a[i][2]+1 == b[j][2]):
					res.append(a[i][0])
				j += 1
		i+= 1
	res = set(res)
	for i in res:
		print(i, stories_index[i], sep=" : ")
	return res

def merge2(a, b):
	l1 = len(a)
	l2 = len(b)
	l = min(l1, l2)
	res = []
	i = 0
	j = 0
	while i<l1: #optimize
		for j in range(0, l2):
			if(a[i][0] == b[j][0]):
				#print(a[i][1], b[i][1], sep = " : ")
				#print(a[i][2], b[i][2], sep = " : ")
				if(a[i][1]+1 == b[j][1] and a[i][2]+1 == b[j][2]):
					res.append(a[i][0])
				j += 1
		i+= 1
	res = set(res)
	
	return res

def phrase2(w):
	l = len(w)-1
	m = []
	for i in range(0,l):
		#print("k")
		a = phrase3(w[i], w[i+1], 1)
		m.append(a)
	#print(m)
	l = len(m)
	k = []
	if(l==1):
		for i in m[0]:
			k.append(i[0])
			#print(i[0], stories_index[i[0]], sep=" : ")
		k = set(k)
		for i in k:
			print(i, stories_index[i], sep=" : ")
	else:
		l = len(m)-1
		for i in range(0,l):
			merge(m[i], m[i+1])

def phrase5(w):
	l = len(w)-1
	m = []
	for i in range(0,l):
		#print("k")
		a = phrase3(w[i], w[i+1], 1)
		m.append(a)
	#print(m)
	l = len(m)
	k = []
	if(l==1):
		for i in m[0]:
			k.append(i[0])
		k = set(k)
		
		
	else:
		l = len(m)-1
		for i in range(0,l):
			k = merge2(m[i], m[i+1])
	return k
#phrase2(["one", "day"])

def process_query():
	q = input("Enter the query: ").strip()
	if('/' in q):
		#print(q)
		q = q.lower()
		q = q.split(" ")
		n = int(q[1][1])
		phrase(q[0], q[2], n)

	else:
		q = q.split(" ")
		#print(q)
		m_l = len(q)
	
		if(m_l == 1):
			search_single(q[0])
		elif(m_l == 3 and (("AND" in q) or ("OR" in q))):
			if(q[1]=="AND"):
				search_and(q[0].lower(), q[2].lower())
			if(q[1]=="OR"):
				search_or(q[0].lower(), q[2].lower())
		else:
			#q = q.lower()
			
			if("AND" in q):
				e = q.index("AND")
				q1 = q[0:e]
				q2 = q[e+1:]
				#print(q1)
				#print(q2)
				a = []
				b = []
				for i in q1:
					a.append(i.lower())
				for i in q2:
					b.append(i.lower())
				x = phrase5(a)
				y = phrase5(b)
				#print(x)
				#print(y)
				res = []
				for i in x:
					if i in y:
						res.append(i)
				#print()
				for i in res:
					print(i, stories_index[i], sep=" : ")
					
					
			else:
				s = []
				for i in q:
					s.append(i.lower())
			
				phrase2(s)
				
			

			
process_query()

		

#phrase("why","you", 2)
			



