#functions with paramters for list
def ds1(rollno,name):
    print("Inside function for List... ")
    address="mumbai"
    l1=[rollno,name]
    print(l1)
    l1.append(address)
    print(l1)
    l1.remove(address)
    print("removed address successfully...")
    print("Element popped :",l1.pop(-2))
    l1.clear()
    print("Cleared List...")
    del l1
    print("deleted dectionary successfully...")
    print("function ended successfully...")
    print("-----------------------------")

#functions with parameters for a dictionary
def ds2(rollno,name):
    print("Inside function for Dictionary...")

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

    #print(d1)
    print("Values changed during runtime...")

    del d1
    print("deleted dectionary successfully...")
    print("function ended successfully...")
    print("-----------------------------")

#functions with parameters for tuple
def ds3(rollno,name):
    print("Inside Function for Tuple...")
    t1=(rollno,name)
    print("Tuple :",t1)
    print("Updated tuple :",t1+("name","contact"))
    num=t1.count("name")
    print("No. of times name is repeated : ",num)
    del t1
    print("Tuple deleted successfully...")
    print("function ended successfully...")
    print("-----------------------------")

#functions with parameters for sets
def ds4(rollno,name):
    print("Inside the function for Sets...")
    s1={rollno,name}
    print("Current set :",s1)
    #creating empty set
    s2=set()
    print(s2)
    #updating second set
    s2.add("address")
    print("added address successfully")
    print("changing address to contact")
    s2.update("contact")
    print("Updated List :",s2)
    s2.discard("contact")
    print("Discarded Contact from set2...")
    del s1
    del s2
    print("Now deleted both sets")
    print("function ended successfully...")
    print("-----------------------------")

#passing parameters while calling the function
ds1(42,'AtharvBowlekar') #list function
ds2(43,'AryanYewale')    #dictionary function
ds3(41,'MitaliRane')     #tuple function
ds4(46,'AryanPandit')    #sets function