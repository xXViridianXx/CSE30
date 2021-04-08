import sys

# def bit(n, k, binary = [], string = ''):
#
#     if n>0:
#         bit(n//k, k)
#         # binary.append(str(n%k))
#         return string + str(n%k)
#
#
#     for i in binary:
#         string += i
#     if len(binary) <= 1:
#         return 0
#
#
#
#     return string
#
#
#
# n = int(sys.argv[1])
# k = int(sys.argv[2])
#
# print(bit(n, k))
def printWords(start, end):
    print(f'{start} --> {end}')


def hanoi(n, start, end):
    if n == 1:
        printWords(start, end)
        return 1
    other = 6 - (start + end)
    hanoi(n-1,start,other)
    printWords(start, end)
    hanoi(n-1,other, end)

hanoi(3, 1, 3)
