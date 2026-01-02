#classes and objects
class IfB2:
    def __init__(self):         #constructor initialization
        str="This is IfB2"      #str inside a constructor
        self.str=str            #helps to make str globalized variable so
                                #that it can be accessed outside the const
    def display(self):
        print(self.str)

if_b2=IfB2()        #object initialization
if_b2.display()     #function called using object