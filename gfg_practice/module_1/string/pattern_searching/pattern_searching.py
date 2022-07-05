
def search_pattern(txt: str, pat: str):
    """Search the pattern in the string

    Args:
        txt (str): large text
        pat (str): pattern to be searched

    Returns:
        _type_: output
    """

    my_locations = []

    fo = check_if_substring_by_loop(txt, pat, 0, len(txt))
    my_locations.append(fo)
    while fo >=0:
        print(fo)
        fo = check_if_substring_by_loop(txt, pat, fo+1, len(txt))
        if(fo!=-1):
            my_locations.append(fo) 

    return my_locations

def check_if_substring_by_loop(s1, s2, start, end):

    substr_ctr = 0

    fo = True
    save_fo = None

    for i in range(start, end):
        if(substr_ctr==len(s2)):
            break
        if(s2[substr_ctr]==s1[i]):
            substr_ctr+=1
            if(fo):
                save_fo = i
                fo = False
        else:
            substr_ctr=0

    return save_fo if substr_ctr==len(s2) else -1

def driver():
    print(search_pattern("geeks for geeks", "geeks"))

if(__name__==r"__main__"):
    driver()