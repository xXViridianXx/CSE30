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

	for i in range(0, len(L)):
		if string == '{':
			string += f'{L[i]}'
		else:
			string += f', {L[i]}'
	if len(L) < 1:
		return '{ }'
	string += '}'

	return string

def usage(word):
	print(f"cannot parse '{word}' as int", file=sys.stderr)
	print('Usage: python3 Subset.py n k (where 0<=k<=n)', file=sys.stderr)

def usage_single():
	print('Usage: python3 Subset.py n k (where 0<=k<=n)', file=sys.stderr)

if __name__=='__main__':
	if 1 < len(sys.argv) <= 3:
		n = sys.argv[1]
		if n.strip().isdigit():
			n = int(n)
			if len(sys.argv) == 3:
				k = sys.argv[2]
				if k.strip().isdigit():
					k = int(k)
					if k > n or k < 0:
						usage_single()
					L = []
					printSubsets(L,n,k,1)
				else:
					usage(k)
			else:
				usage_single()
		else:
			usage(n)
	else:
		usage_single()
