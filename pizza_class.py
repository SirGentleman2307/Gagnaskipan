import random

class Pizza_slice(object):

    def __init__(self):
        self.__topings = self.add_topings()
        self.__ID = ''

    def add_topings(self):
        topping_list = ['Pepperoni', 'Mushrooms', 'Onions', 'Sausage', 'Bacon', 'Extra cheese', 'Black olives', 'Green peppers']
        Out_put_list = []
        Out_put_list.append(random.choice(topping_list))
        return Out_put_list

    def __str__(self):
        return str(self.__topings)



class Pizza_box(object):

    def __init__(self, pizza_list = []):
        self.__list = pizza_list

pizza = Pizza_slice()
print(pizza)

