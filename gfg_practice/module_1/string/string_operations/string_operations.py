my_str = "some random string"

print(my_str.upper())
print(my_str.lower())
print(my_str.isupper())
print(my_str.islower())
print(my_str.startswith("some"))
print(my_str.endswith("ing"))
print(my_str.startswith("some",0,len(my_str)))
print(my_str.endswith("ing",len(my_str)-5,len(my_str)))

# by default split method splits arround spaces
my_str2 = "some,random,string"
print(my_str.split())
print(my_str2.split(","))

l = ['some', 'random', 'string']


# joiner.join function
print("--".join(l))

my_str3 = "--some,random,string--"

print(my_str3.strip("-"))
print(my_str3.lstrip("-"))
print(my_str3.rstrip("-"))



s1 = "some random string"

s2 = "some"
# find works like the index function but the only difference is
# it does not give an exception if the value is not found
print(s1.find(s2))
print(s1.find("some"))
print(s1.find("3423"))
print(s1.find("some", 0, len(s1)))