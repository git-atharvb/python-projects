#multilevel inheritance
class A:
    def display(self):
        print("This is class A...")

class B(A):             #passing parameter provides
    def display1(self):
        print("This is class B...")
class C(B):
    def display(self):
        return super().display()
    def display1(self):
        return super().display1()
    def display2(self):
        print("This is class C...")
b=B()
b.display()
print("------------")
# a=A()
# a.display()
# print("------------")
c=C()
c.display()
c.display1()
c.display2()