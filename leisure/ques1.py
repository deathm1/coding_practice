def combination(mylist,r):
    if r == 0:
        return [[]]
    L = []
    for i in range(0,len(mylist)):    
        first = mylist[i]
        rem = mylist[i+1:]
        combList = combination(rem,r-1)
        for x in combList:
            L.append([first]+x)
    return L        
def sumofProduct(N, A):
    l=[]
    out = 0
    for i in range(1, A+1):
        l.append(combination(N, i))
        my_list = combination(N, i)

        for elem in my_list:
           out = out + max(elem) * min(elem)
    return out

print(sumofProduct([1,2,1], 3))