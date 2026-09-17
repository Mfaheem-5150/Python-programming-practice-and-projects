x = int(input("enter first num: "))
y = float(input("enter second num: "))
op =str(input("enter operator: "))
if(op=="+"):
     print(x+y)
elif(op=="-"):
     print(x-y)
elif(op=="*"):
     print(x*y)
elif(op=="**"):#power operator
     print(x**y)
elif(op=="/"):
     print(x/y)
else:
     print("invalid operator")
    