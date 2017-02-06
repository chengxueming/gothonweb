'''
W = "white"
m = {}
for i in range(1,11):
	m[i] = W
print m

q = {1:1,2:2,3:3}
key = 3
if key in q:
	print q[key]
'''
global score
score = 1

def fa():
	global score
	score = 3
fa()
print score