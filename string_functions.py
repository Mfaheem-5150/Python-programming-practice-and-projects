str="i am coder"
print(str.capitalize())

'''str.capitalize does not modify the original string so if we want 
to modify the original string then we write as '''
str=str.capitalize()
print(str)
# str.endswith()return True if substr match and return -1 if does not match
print(str.endswith("r"))
print(str.endswith("er"))
print(str.endswith("coder"))
print(str.endswith("programer"))

# str.find() is use for finding the particular substr.
# if find the return starting index

print(str.find("am"))
print(str.find("c"))

# str.replace() function replace the new string with old one like
str="I am studing python right now form apna college"
print(len(str))
str=str.replace("python","HTML")
print(str)
# we can write as well
print(str.replace("HTML","Java script"))
# str.count() return the numbers of occurence of substr
str="hello,hello my name is M.faheem"
print(str.count("hello"))