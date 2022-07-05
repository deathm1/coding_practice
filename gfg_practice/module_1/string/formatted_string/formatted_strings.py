#old way
my_str1 = "Hi, How are you %s and %s"%("asdasd","ASdfas2")
print(my_str1)


# using format function
my_str2 = "Hi, How are you {0} and {1}".format("val1","val2")
print(my_str2)


# using f string
var1 = "val1"
var2 = "val2"
my_str3 = f"Hi, How are you {var1} and {var2}"
print(my_str3)


# using f string with expressions also methods can be called
var1 = "val1"
var2 = "val2"
my_str4 = f"Adding {var1} and {var2} = {var1+var2} {var1.upper()}"
print(my_str4)