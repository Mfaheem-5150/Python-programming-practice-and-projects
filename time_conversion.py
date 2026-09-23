seconds=int(input("Enter the numbers of seconds : "))
hours=0
mint=int(seconds/60)
seconds=int(seconds%60)
if(mint>=60):
     hours=int(mint/60)
     mint=int(mint%60)
if(hours>12):
    hours=hours+1

print("Hours: ",hours)
print("Mintues: ",mint)
print("Seconds: ",seconds)
