import string
def read_word_list(word):
	word_list = dict()
	fout = open(word, "r")
	for line in fout:
		line = line.split()
		for index in range(0,len(line)):
			word_list[index] = word_list.get(index,0) + 1
	return word_list

def open_book(book):
	
	d1 = dict()
	
	fout = open(book, "r",encoding="utf8")
	for line in fout:
		line = line.split()
		for index in range(0,len(line)):
			word = line[index].strip(string.whitespace + string.punctuation)
			d1[word] = d1.get(word,0) + 1
	return d1
	
def cmp_dicts(word_list, book):
	for b_word in book.keys():
		if(b_word not in word_list):
			print(b_word)



word_dict = read_word_list("words.txt")
book_dict = open_book("book_1.txt")

cmp_dicts(word_dict, book_dict)