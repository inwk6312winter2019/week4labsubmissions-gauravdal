import string
def read_by_word():
	
	d1 = dict()
	
	fout = open("book_1.txt", "r",encoding="utf8")
	
	for line in fout:
		line = line.split()
		for index in range(0,len(line)):
			word = line[index].strip(string.whitespace + string.punctuation)
		

			print(word)
		


