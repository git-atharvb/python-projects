'''
#ASCII values
var="a"
print(ord("a"))
var="A"
print(ord("A"))
print(chr(66))
print(chr(89))
'''

#for loops
for i in 0,1,2,3,4:
    if i%2==0:
        print("odd",i)
print("-----------------")
for j in range(0,11,2):
    if j%2==0:
        print("even",j)
print("----------------")
for k in range(11,-1,-1):
    if k%2==0:
        print("odd",k)
