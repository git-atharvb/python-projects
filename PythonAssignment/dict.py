#accepting data from user and printing a dictionary
'''
rollno=int(input("Enter your roll no :"))
name=input("Enter your name :")
address=input("Enter your address :")
'''
d1={
    'key1':'rollno',
    'key2':'name'
}
print(d1)
print(d1["key1"])
print(d1["key2"])

#adding elements  in existing dictionary
d1["key3"]='address'
print(d1)

#printing all the keys
print(d1.keys())
#printing all the values
print(d1.values())

#updating dictionary keys and values
d1.update({"year":2023})
print(d1)

#deleting keys and values
d1.popitem()
print(d1)
 
print("-------------")
#forloop
for i in d1.keys():
    print(i)

for j in d1.values():
    print(j)

print("------------")

#printing together keys and vlaues
for i,j in d1.items():
    print(i,j)