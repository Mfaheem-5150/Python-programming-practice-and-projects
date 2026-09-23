tup=[1,4,9,16,25,36,49,64,81,100]
num=int(input("Enter a number to search: "))
# print(len(tup))
end=int(len(tup))
i=0
while i < end:
    if(num==tup[i]):
        print("number is founded.")
        break
    i+=1
if(i == end):
      print("Not found.")
print("program ended.")
