#list ->to add element in existing list use "append","insert","extend"
ls=[6,7,8,9]
ls.append(10)
print(ls)
ls.insert(1,2)
print(ls)
ls1=[3,4,5]
ls.extend(ls1)
print(ls)
print("-----------------")
#to remove element from existing list use "remove","pop","clear"
ls.remove(5)
print(ls)
print(ls.pop(-1))
print(ls)
ls.clear()
print(ls)
print("List cleared successfully. It is now empty...")
print("-----------------")

#using in-built functions for list operations 
listA=[1,5,3,9,7]
print("New List :",listA)
print("Sum of elements in list :",sum(listA))
print("Smallest value in list :",min(listA))
print("Largest value in list :",max(listA))
print("List in ascending order :",sorted(listA))
listA.sort(reverse=True)
print("List in descending order :",listA)

print("-----------------")
#converting list into a tuple
new_tuple=tuple(listA)
print("Tuple conversion of list :",new_tuple)

#deleting a existing list
del listA
print("List deleted successfully...")
print("Trying to print the deleted list will display an Error...")
#print(listA)
