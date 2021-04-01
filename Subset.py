import sys

# class Pascals:

	# def __init__(self, n, k):
	# 	self.n = n
	# 	self.k = k
	# 	self.B = ['*']


def createSet(n):
	set = []
	for i in range(1, n+1):
		set.append(i)



# def bitList(n):
# 	B = ['*']
# 	for i in range(1, n+1):
# 		B.append(i)
# 	return B

def printSubsets(set, B, k, i=1):
	zet = set

	if k > 0:
		l = set
		r = set
		B.append(1)
		printSubsets(zet, )

			
	print(B)
	# print(l)



if __name__=='__main__':
	n = int(input())
	k = int(input())

	
	createSet(n)
	# p.bitList()
	printSubsets(createSet(n), ['*'], k)
