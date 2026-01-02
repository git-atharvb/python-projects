#function with no parameters

def ds():
    print("Inside function DS...")
    print("* This function accepts rollno and name *")
    rollno=int(input("Enter your roll no :"))
    name=input("Enter your name :")

    d1={
    'key1':rollno,
    'key2':name
    }
    #print(d1)
    print("Your roll-no is : ",d1["key1"])
    print("Your name is : ",d1["key2"])

    #change name in runtime
    d1.update({name:'XYZ'})
    print("Your name is changed to : ",d1[name])

    # #adding address also
    # address=input("Enter your address : ")
    # d1["key3"]=address
    # print(d1)
    print("Values changed during runtime...")

    del d1
    print("deleted dectionary successfully...")
    print("function ended successfully...")

ds()
