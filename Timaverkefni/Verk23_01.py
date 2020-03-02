

def calc_len(a_list, count = 0):

    if a_list == []:
        return count
    else:
        count += 1
        return calc_len(a_list[:-1], count)

# print(calc_len(list('ABCDEFG')))

def lin_search(a_list, num_to_find):

    INDEX = len(a_list) // 2
    if a_list == []:
        return False

    print(a_list,len(a_list))

    if a_list[INDEX] == num_to_find:
        return len(a_list)
    else:
        num_to_check = a_list[INDEX]
        if num_to_check > num_to_find:
            return lin_search(a_list[:INDEX - 1], num_to_find)
        else:
            return lin_search(a_list[INDEX + 1:], num_to_find)

a_list = [1,4,5,7,8,9,10,15,20,24]
print(lin_search(a_list,20))

def count_ins(a_list, num_to_find):

    if lin_search(a_list, num_to_find):
        pass