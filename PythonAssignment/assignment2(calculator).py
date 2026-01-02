#MENU DISPLAY OF CALCULATOR
print("---CALCULATOR *---")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVISION")
print("5. MODULES")
print("6. EXPONENTIAL")
print("7. FLOOR DIVISION")
print("------------------")

#Enter what you want to perform
ch=int(input("* ENTER YOUR CHOICE * ---->"))
if ch==1:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a+b
    print("Addition of A and B = ",c)
elif ch==2:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a-b
    print("Subtraction of A and B = ",c)
elif  ch==3:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a*b
    print("Multiplication of A and B = ",c)
elif ch==4:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a/b
    print("Division of A and B (Quotient) = ",c)
elif ch==5:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a%b
    print("Modulas of A and B (Remainder) = ",c)
elif ch==6:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a**b
    print("Exponential of A to B (Power) = ",c)
elif ch==7:
    a=int(input("Enter value of A :"))
    b=int(input("Enter value of B :"))
    c=a//b
    print("Floor Division of A and B (whole number result) = ",c)
else:
    print("Enter choice between 1 to 7....")