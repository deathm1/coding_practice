def check_if_substring_by_loop(s1, s2):

    substr_ctr = 0

    for i in range(0, len(s1)):
        if(substr_ctr==len(s2)):
            break
        if(s2[substr_ctr]==s1[i]):
            substr_ctr+=1
        else:
            substr_ctr=0

    return True if substr_ctr==len(s2) else False
    


def check_if_substring(s1, s2):
    return s2 in s1

def driver():
    print(check_if_substring("abcdef","abc"))
    print(check_if_substring_by_loop("geeksforgeeks", "ee"))


if(__name__=="__main__"):
    driver()