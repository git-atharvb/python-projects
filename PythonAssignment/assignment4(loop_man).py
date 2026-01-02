#for else loop on a string
str="ENVIRONMENT FRIENDLY"
for s in str:
    if s=="R":
        print("IF statement")
else: 
    print(s)
print("----------------------------")
#while else loop on a string
flag=0
while (flag < 10):      
    flag = flag + 3  
    print("While executed successfully")
else:  
    print("Else statement executed successfully")  
print("----------------------------")
#break statement use
for string in "IMMEDIATELY":  
    if string == 'L':
         print("L letter founded, break is executed")  
         break  
    print('Current Letter: ', string)  
print("----------------------------")
#continue statement use
for string in "Hello World Programming":  
    if string == "o" or string == "o" or string == "g":  
         continue  
    print('Current Letter:', string) 
print("----------------------------")
#pass statement use
for string in "Hello World Programming":  
    pass  
print( 'Last Letter:', string) 