marks=[243,778,445,304,289]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# with the help of list we can also modify the element of the list
marks[3]="muhammad faheem"
print(type(marks))
print(marks)
student=["faheem","layyah",20,456]
print(student)
print(type(student)) 
print(len(marks))
print(len(student))
list1=[78,98,67,56,57,37,87,79,80]
print(len(list1))
list1.sort()
print(list1)
#if we write the code like that .
# it  return the None so "sort()" modify original list
# print(list1.sort())

# List slicing syntax: list_name = [starting_idx : ending idx]
print(list1[1:4])
print(list1[:5])#by default start from 0 index 
print(list1[0:])#by default end at last index 
