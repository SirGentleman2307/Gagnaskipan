import math

class Pizza:
    def __init__(self, name, topping_1, topping_2 = None, topping_3 = None):
        self.__name = name
        self.__served = False
        self.__toppings = []
        self.add_toppings(self.__toppings, topping_1, topping_2, topping_3)

    def __str__(self):
        toppings_str = ", ".join(self.__toppings)
        served_str = "served" if self.__served else "unserved"
        return f"{self.__name}: with {toppings_str} that is {served_str}"

    def get_name(self):
        return self.__name

    def get_toppings(self):
        return self.__toppings

    def get_served(self):
        return self.__served

    def add_toppings(self, toppings_list, topping_1, topping_2, topping_3):
        for topping in [topping_1, topping_2, topping_3]:
            if topping:
                self.__toppings.append(topping)

    def set_served(self, bool_val):
        self.__served = bool_val
        

class Pizza_system(object):

    def __init__(self):
        self.__dict = {}
        self.__unique_number = {}

    def make_ID(self, pizza_obj):
        pizza_name_str = pizza_obj.get_name()
        unique_number_str = self.get_unique_number(pizza_name_str)
        self.__unique_number[pizza_name_str]
        return pizza_name_str[:3].upper() + unique_number_str

    def get_unique_number(self, pizza_name_str):
        try:
            self.__unique_number[pizza_name_str] += 1
        except:
            self.__unique_number[pizza_name_str] = 1
        number_of_digits = int(math.log10(self.__unique_number[pizza_name_str]))
        return ("0")*(3-number_of_digits) + str(self.__unique_number[pizza_name_str])

    def add_Pizza(self, pizza_obj):
        self.__dict[self.make_ID(pizza_obj)] = pizza_obj

    def mark_pizza(self,ID_input):
        self.__dict[ID_input].set_served(True)

    def show_all_pizza(self):
        for id,pizza in sorted(self.__dict.items()):
            print(f"Pizza with id: {id}:\n" + str(pizza))

    def remove_served_pizza(self):
        for id,pizza in sorted(self.__dict.items()):
            if pizza.get_served():
                del self.__dict[id]

    def __str__(self):
        return str(self.__dict)
