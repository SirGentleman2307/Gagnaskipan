def bin_search(a_list, num_int):

    if a_list == []:
        return 0

    INDEX = len(a_list) // 2
    MID = a_list[INDEX]
    print(a_list, len(a_list), INDEX, MID, num_int)

    if MID == num_int:
        return len(a_list) - INDEX

    if MID < num_int:
        return len(a_list) - bin_search(a_list[INDEX + 1:], num_int)
    else:
        return len(a_list) - bin_search(a_list[:INDEX], num_int)


a_list = [1,4,5,7,8,9,10,15,20,24,27]
print(bin_search(a_list,4))
print(a_list[bin_search(a_list,4)])
