
def check_anagram(s1 : str, s2 : str):
    if(len(s1) != len(s2)):
        return False
    
    count_unicode = [0] * 256

    for i in range(len(s1)):
        count_unicode[ord(s1[i])] +=1
        count_unicode[ord(s2[i])] -=1
    

    # constant work as we have already declared the array of 256
    for x in count_unicode:
        if(x!=0):
            return False

    return True 
    


def driver():
    print(check_anagram("b","d"))

if(__name__==r"__main__"):
    driver()