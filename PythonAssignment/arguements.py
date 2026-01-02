#keyword arguements to accept n no. of parameters
#will print inside a dictionary i.e. {} brackets
def display(**a):
    print(a)

display()
display(name="atharv",rollno=42)

#variable arguements to accept n no. of parameters
#will print inside a tuple i.e. () brackets
def display1(*a):
    print(a)

display1()
display1(1)
display1([1,2,3,4],5.5)

print("---------------------")

#lambda functions
i=int(input("Enter value :"))
square=lambda i:i**2
print(square[i])