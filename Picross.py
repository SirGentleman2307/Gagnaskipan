

class Game:

    def __init__(self, size = 5):
        self.__Xlist = []
        self.__Ylist = []
        self.__Size = size
        self.__GameBord = self.start_bord()

    def start_bord(self):
        return [[0] * self.__Size for _ in range(self.__Size)]

    def display(self):
        dis_str = ''
        for X in self.__GameBord:
            dis_str += '\n'
            for Y in X:
                if Y == 0:
                    dis_str += '░ '
                if Y == 1:
                    dis_str += '▓ '
        print(dis_str)

    def edit(self, X, Y, value):
        self.__GameBord[X -1][Y -1] = value

    def __str__(self):
        return '\n'.join([str(element) for element in self.__GameBord])


Cross2 = Game(15)
print(Cross2)
Cross2.edit(1,1,1)
Cross2.edit(2,1,1)
Cross2.edit(4,1,1)
Cross2.edit(1,5,1)
Cross2.edit(1,2,1)
Cross2.display()
