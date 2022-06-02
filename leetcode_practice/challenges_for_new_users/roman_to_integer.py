def romanToInt(s: str):
    roman = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    # this is reverse for loop in python 
    # range function takes start, stop and step as arguments.
    ans = 0
    for i in range(len(s)-1,-1,-1):
        #get number from dictionary
        num = roman[s[i]]
        print("i cn: ", s[i],"ans : ", ans)
        # check if number before current number is not greater or equal to / than current number
        if (4*num<ans): 
            ans = ans - num
        else: 
            ans = ans + num
        print("f cn: ", s[i],"ans : ", ans)
        print("\n")
    return ans

print(romanToInt("CMDM"))



# for LVIII
# i cn:  I ans :  0
# f cn:  I ans :  1


# i cn:  I ans :  1
# f cn:  I ans :  2


# i cn:  I ans :  2
# f cn:  I ans :  3


# i cn:  V ans :  3
# f cn:  V ans :  8


# i cn:  L ans :  8
# f cn:  L ans :  58


# 58

# for MCMXCIV
# i cn:  V ans :  0
# f cn:  V ans :  5


# i cn:  I ans :  5
# f cn:  I ans :  4


# i cn:  C ans :  4
# f cn:  C ans :  104


# i cn:  X ans :  104
# f cn:  X ans :  94


# i cn:  M ans :  94
# f cn:  M ans :  1094


# i cn:  C ans :  1094
# f cn:  C ans :  994


# i cn:  M ans :  994
# f cn:  M ans :  1994


# 1994
