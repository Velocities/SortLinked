from bin.Node import *
from bin.scripts.main import *

h = Node(6, Node(1, Node(2)))
b = Solution()
ans = b.sortLink(h)
final = []
getVals(ans, final)
for i in final:
	print(i)
