import sys


def printSubsets(B,k,i):
	if (k == 0 or k == len(B) -1) and 1 in B:
		print(to_string(B))
	if k <= (len(B) -1) -i +1 and k > 0:

		B[i] = 1
		printSubsets(B, k-1, i+1)
		B[i] = 0
		printSubsets(B, k, i+1)

def to_string(B):

	string = '{'

	for i in range(1, len(B)):
		if string == '{' and B[i] == 1:
			string += f'{i}'
		elif B[i] == 1:
			string += f',{i}'
	if 1 not in B:
		return '{ }'
	string += '}'

	return string

if __name__=='__main__':
	n = sys.argv[1]
	if n.strip().isdigit():
		n = int(n)
		if len(sys.argv) == 3:
			k = sys.argv[2]
			if k.strip().isdigit():
				k = int(k)
				B = ['*']
				if k == 0:
					print('{ }')
				for i in range(1, n+1):
					B.append(0)
				printSubsets(B, k, 1)
