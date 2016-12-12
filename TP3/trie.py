def tree():
	return [0,[None]*256]


def add_word(word):
	global root
	current = root
	for ch in word:
		if current[1][ord(ch)] == None:
			current[1][ord(ch)] = tree()
		current[0] += 1
		current = current[1][ord(ch)]

def find_word(word):
	global root
	current = root
	for ch in word:
		if current[1][ord(ch)] == None:
			return 0
		else:
			current = current[1][ord(ch)]
	return current[0]
	
root = tree()

n = int(input())
prefijos = []
for word in range(n):
	s,l = input().split()
	l = int(l)
	add_word(s)
	prefijos.append(s[0:min(l,len(s))])

maximo = -1
for prefijo in prefijos:
	p_under = find_word(prefijo)
	if p_under > maximo:
		maximo = p_under
print(maximo)
