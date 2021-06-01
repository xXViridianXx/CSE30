#------------------------------------------------------------------------------
#  MultipleInheiritance.py
#  Illustrate multiple inheiritance.
#------------------------------------------------------------------------------


class Class1:

    def m(self):
        print("   in Class1")
        print("   in Class1")


class Class2(Class1):

    def m(self):
        print(" in Class2")
        super().m()
        print(" in Class2")


class Class3(Class1):

    def m(self):
        print("  in Class3")
        super().m()
        print("  in Class3")


class Class4(Class2, Class1):

    def m(self):
        print("in Class4")
        super().m()
        print("in Class4")


def main():

   x = Class4()
   y = Class3()
   z = Class2()

   print()
   x.m()
#    print()
#    y.m()
#    print()
#    z.m()

   print()
   print(f'method resolution order for {type(x).__name__}')
   for c in type(x).mro():
      print(c.__name__)
   # end

   print()
   #print(Class1.mro())
   #print(Class2.mro())
   #print(Class3.mro())
   #print(Class4.mro())
   #print()


# end


#------------------------------------------------------------------------------
if __name__ == '__main__':

   main()

# end
