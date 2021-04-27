import sys

def base7digits(n):

   if n>0:
      base7digits(n//7)
      print(n%7, sep='',end='')
   # end
# end

base7digits(7)

def sequence_gen(a,b):
    i = 1
    while True:
        if i*a % b == 1:
            yield a*i
        i+=1

sequence_gen(3,5)

A = sequence_gen(3,5)

for i in range(15):
    s = " {0:<12}".format(next(A))
    print(s)
    # end
print()
