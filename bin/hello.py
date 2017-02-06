#print None
'''
0
1 2 3 4
56 7
9	610
'''
l = {}
l[0] = [1,2,3,4]
l[1] = [5,6]
l[2] = [7]
l[5] = [9]
l[8] = [6,10]

B = "black"
W = "white"
def BFS(l):
	m = {}
	for i in range(0,11):
		m[i] = {"c":W,"d":-1}
	m[0]["d"] = 0
	q = [0]
	while q.__len__() > 0:
		if q[-1] in l:
			for i in l[q[-1]]:
				if m[i]["c"] == W:
					q.insert(0,i)
					m[i]["d"] = m[q[-1]]["d"] + 1
		m[q[-1]]["c"] = B
		q.pop()
	return m
'''
def sub(l,m,node):
	if node not in l:
		return
	for i in l[node]:
		if m[i]["c"] == W:
			#print l[i]
			sub(l,m,i)
			m[i]["c"] = B
def DFS(l):
	m = {}
	for i in range(0,11):
		m[i] = {"c":W,"d":-1}
	m[0]["d"] = 0
	sub(l,m,0)
	return m
'''
global score
score = 1
def sub(l,m,node):
	print "node:" + str(node)
	global score
	if m[node]["c"] == W:
		m[node]["begin"] = score
	else:
		return
	if node in l:
		for i in l[node]:
			if m[i]["c"] == W:
				sub(l,m,i)
				m[i]["c"] = B
	score += 1
	m[node]["stop"] = score
def DFS(l):
	m = {}
	for i in range(0,11):
		m[i] = {"c":W,"begin":0,"stop":0}
	score = 0
	for i in range(0,11):
		sub(l,m,i)
	return m

if __name__ == "__main__":
	'''
	m = BFS(l)
	print m
	'''
	print DFS(l)

