import copy
import sys
AI = 1
PLAYER = 2
chessboard = [[0 for x in range(1,15)] for x in range(1,15)]
chessboard[3][2],chessboard[3][1] = PLAYER,AI

cb2 = copy.deepcopy(chessboard)
cb2[0][0] = AI
#print "\n".join(str(x) for x in chessboard)
print "*"*50
#print "\n".join(str(x) for x in cb2)

root = {"chessboard":chessboard,"score":10,"parent":None}
node2 = {"chessboard":cb2,"score":20,"parent":root}
cb3 = copy.deepcopy(cb2)
cb3[0][1] = PLAYER
node3 = {"chessboard":cb3,"score":15,"parent":root}
print sys.getsizeof(node2["chessboard"])
print sys.getsizeof(node3)