import string

def sed(pat_str, rep_str, f1, f2):
	
	try:
		fout = open(f1, "r")
		fin = open(f2, "w+")
		for line in fout:
			if(pat_str in line):
				line = line.replace(pat_str, rep_str)
			fin.write(line)
		
		fout.close()
		fin.close()
		
	except:

		print("File operation doesn't take properly")
		
file1 = "file1.txt"
file2 = "file2.txt"
sed("aaa","bbb", file1, file2)
print("file operation is successfully done")