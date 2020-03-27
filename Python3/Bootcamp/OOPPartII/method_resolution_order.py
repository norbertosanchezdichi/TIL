class A:
    def do_something(self):
        print("Method Defined In: A")
        
class B(A):
    def do_something(self):
        print("Method Defined In: B")
        
class C(A):
    def do_something(self):
        print("Method Defined In: C")
        
class D(B,C):
    pass
    def do_something(self):
        print("Method Defined In: D")
        super().do_something()# calls do_something() for the next class in line of the MRO
 
print(D.__mro)
print(D.mro())
help(D)
        
thing = D()
thing.do_something()