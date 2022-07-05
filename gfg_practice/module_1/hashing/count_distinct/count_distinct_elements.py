def using_set(my_list):
    return len(set(my_list))



def using_for_loop(my_list):
    result = 1

    for i in range(1, len(my_list)):
        if my_list[i] not in my_list[0:i]:
            result+=1
    return result


def driver():
    print(using_for_loop([10,20,10,30,30,20]))
    print(using_set([10,20,10,30,30,20]))

if __name__ == '__main__':
    driver()


