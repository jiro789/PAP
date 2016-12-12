f = open("Sample.txt",'w')

def generate_test1(f):
	s = ""
	for i in range(10**5):
		s += str(2**30-1) + " "
	f.write(str(10**2) + '\n')
	f.write(s)
	result = [int(ch) for ch in s.split()]
	print(sum(result))

def generate_test2(f):
	s = ""
	for i in range(1000):
		s += str(i) + " "
	f.write('100' + '\n')
	f.write(s)
	result = [int(ch) for ch in s.split()]
	print(sum(result))

generate_test2(f)		
