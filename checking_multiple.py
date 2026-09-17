num=int(input("Enter a number : "))
mul=int(input("enter the that you wants to check the multiple: "))

# if(num%7==0):
#     print("Entered number is multiple of 7")
# else:
#     print("Not multiple of 7")
if(num%mul==0):
    print("Entered number is multiple of ",mul)
else:
    print("Not multiple of ",mul)