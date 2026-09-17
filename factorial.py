# program for calculating the factorial of any number entered by the user
i=1  # i is count on loop run 
fact=1
num=int(input("Enter a number to calculate factorial: "))

while i <= num:
    fact=fact*i
    i+=1
print("Factorial : ",fact)