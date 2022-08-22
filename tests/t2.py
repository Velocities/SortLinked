from bin.Node import *
from bin.scripts.main import *

h = Node(10, Node(8, Node(9, Node(7, Node(6, Node(5, Node(1, Node(4, Node(2, Node(3))))))))))
b = Solution()
ans = b.sortLink(h)
final = []
getVals(ans, final)
for i in final:
	print(i)
