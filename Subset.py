#------------------------------------------------------------------------------
#  Aniket Pratap
#  1825275
#  CSE 30-02 Spring 2021
#  la2
#  Subset.py
#------------------------------------------------------------------------------
import sys


def printSubsets(L,n,k,i):
	if (k == 0 or k == n) and len(L) > 0:
		print(to_string(L))
	if k <= n -i +1 and k > 0:
		L.append(i)
		printSubsets(L,n, k-1, i+1)
		L.pop(-1)
		printSubsets(L,n, k, i+1)

def to_string(L):

	string = '{'

	for i in range(1, len(L)):
		if string == '{':
			string += f'{L[i]}'
		else:
			string += f',{L[i]}'
	if len(L) < 2:
		return '{ }'
	string += '}'

	return string

def usage(word):
	print(f"cannot parse '{word}' as an int", file=sys.stderr)
	print('Usage: python3 Subset.py n k (where 0<=k<=n)', file=sys.stderr)

if __name__=='__main__':
	if len(sys.argv) > 1:
		n = sys.argv[1]
		if n.strip().isdigit():
			n = int(n)
			if len(sys.argv) == 3:
				k = sys.argv[2]
				if k.strip().isdigit():
					k = int(k)
					L = ['*']
					if k == 0:
						print('{ }')
					printSubsets(L,n,k,1)
				else:
					usage(k)
		else:
			usage(n)
	elif len(sys.argv) == 1:
		print('Usage: python3 Subset.py n k (where 0<=k<=n)', file=sys.stderr)
