list=[88,98,67,56,77,37,88,80,88,95]
print(len(list))
list.sort()
print(list)
print(list.count(88))
# reverse() only reverse the sequence of values not sort the values
list1=[75,98,67,56,77,69,88,80,86,95]
list1.reverse()
print(list1)
# sort(reverse=True) fuction sort the values in decending order
list1.sort(reverse=True)
print(list1)
# append function insert value at the end of list
list.append(100)
print(list)
#insert() insert the value at given index like
# syntax list_name.insert[index,element]
list2=[1,3,2,11,0,2]
list2.insert(3,100)
print(list2)
# remove() function removes the first occurece of given element
list2.remove(2)
print(list2)

# pop() delete the value from list at given index. sytax list_name.pop(index)
list2.pop(2)
print(list2)