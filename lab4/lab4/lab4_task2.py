import string
def read_by_word(*args):
	list1 = []
	for arg in args:
		list1.append((open_book(arg),arg))
	return list1
	
def open_book(book):
	
	d1 = dict()
	
	fout = open(book, "r",encoding="utf8")
	for line in fout:
		line = line.split()
		print("x")
		for index in range(0,len(line)):
			word = line[index].strip(string.whitespace + string.punctuation)
			d1[word] = d1.get(word,0) + 1
			print(word)
		
	for i,j in d1.items():
		print(i,j,sep=" : ")
	
	sum1 = sum(d1.values())
	print("Total number of words used in a book: " , sum1)
	print("Total number of unique words in book is :",len(d1))
	
	return sum1

book1 = "book_1.txt"
book2 = "book_2.txt"

list1 = read_by_word(book2,book1)


def myfunc(e):
	return e[0]
	
list1.sort(key = myfunc)
print(list1)