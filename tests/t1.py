#!/bin/python3
from bin.Node import Node
from scripts.main import *

h = Node(1, Node(3, Node(5, Node(2, Node(4)))))
b = Solution
ans = b.sortLink(h)
final = []
getVals(ans, final)
for i in final:
	print(i)
