from bin.Node import Node

def getVals(obj, a_list):
	cop = obj
	while cop:
		a_list.append(cop.val)
		cop = cop.next

class Solution:
	def sortLink(self, head):
		myVals = []
		getVals(head, myVals)
		myVals.sort()
		counter = 0
		for i in myVals:
			if counter == 0:
				a = Node(i)
			elif counter == 1:
				tmp = Node(i)
				a.next = tmp
			else:
				tmp.next = Node(i)
				tmp = tmp.next
			counter += 1
		return a
