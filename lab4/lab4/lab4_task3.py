import string



def open_book(book):
	
	d1 = dict()
	
	fout = open(book, "r",encoding="utf8")
	for line in fout:
		line = line.split()
		for index in range(0,len(line)):
			word = line[index].strip(string.whitespace + string.punctuation)
			d1[word] = d1.get(word,0) + 1
	
	return d1
	
def reverse_dict(dict1):
	reverse = dict()
	for word in dict1:
		val = dict1[word]
		reverse.setdefault(val,[]).append(word)
		
	return reverse
	
def sort_dict(reverse_dict1):
	dict2 = dict()
	counter = 1
	for key in sorted(reverse_dict1.keys(), reverse = True):
		if (counter <=20):
			print(str(key)+ ":",reverse_dict1[key])
			counter += 1

	

def frequently_used(dict2):
	counter = 1
	for key in dict1:
		if(counter<=20):
			print(str(key)+":"+str(dict1[key]))
		else:
			break
		counter = counter + 1
	
	


book1 = "book_1.txt"
dict1 = open_book(book1)

reverse_dict1 = reverse_dict(dict1)

sort_dict(reverse_dict1)




print()







	




