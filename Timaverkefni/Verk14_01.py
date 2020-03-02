import random


def power(num1, num2):
    print(num1**num2)

def get_int():
    num1, num2 = input('Enter in two numbers: ').split(',')
    num1 = int(num1)
    num2 = int(num2)
    return num1, num2

def power_main():
    '''O(n)'''
    x,y = get_int()
    power(x,y)

def multi_main():
    '''O(n)'''
    x,y = get_int()
    the_sum = 0
    for _ in range(x):
        the_sum += y
    print(the_sum)

def rando_main():
    '''O(n)'''
    a_list = [0]*10
    for i in range(len(a_list)):
        a_list[i] = str(random.randint(1,6))
    return a_list

def printer_main():
    a_list = rando_main()
    print(','.join(a_list))


printer_main()
