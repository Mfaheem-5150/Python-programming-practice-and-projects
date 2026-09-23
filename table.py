
num=int(input("Enter a number to print table : "))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i+=1
print("Program ended.")

# second more efficient program
'''
num=int(input("Enter a number to print table : "))
end_count=int(input("Enter the count to stop the loop: "))
i=1
while i<=end_count:
    print(num,"*",i,"=",num*i)
    i+=1
print("Program ended.")
'''