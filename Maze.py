
def maze_maker(number_int):
    '''Makes a matrx N*N were every thing is int 0'''
    out_list = []
    for _ in range(number_int):
        out_list.append([0] * number_int)
    return out_list

def maze_printer(maze_list):
    '''Prints out a maze'''
    print(' _' * len(maze_list), end='\n')
    for _ in maze_list:
        print('|_' * len(maze_list), end='|\n')


maze_list = maze_maker(2)

maze_printer(maze_list)
print(maze_list[0],len(maze_list))


