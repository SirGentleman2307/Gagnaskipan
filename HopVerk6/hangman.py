import random

class Game:

    def __init__(self, word = '', guesses = 10):
        self.word = word
        self.guesses = guesses
        self.progress = '_ ' * len(self.word)
        self.guessed_ch = []

    def display(self):
        '''Used to display the game state'''
        print('======================\n')
        print('\n\n' + self.progress + '\n\nWord length: ' + str(len(self.progress)//2) + '\nGuesses left: ' + str(self.guesses) + '\n')
        print('Already used charavters: \n' + ', '.join(self.guessed_ch) + '\n\n')

    def check_inp(self, inp):
        '''Checks the given input to be a single character'''
        if len(inp) != 1:
            print('Please input a single character !!!')
            return True

        if inp.isalpha():
            if inp.lower() in self.guessed_ch:
                print('Character has already been used !!!')
                return True
            return False

    def make_guess(self, inp):
        '''Puts given input in the progress string, if the word contains the given input'''
        inp = inp.lower()
        self.guessed_ch.append(inp)

        if inp in self.word:
            for i in range(len(self.word)):

                if self.word[i] == inp:
                    temp = self.progress.split(' ') # Easy to use a list to insert
                    temp[i] = inp                   # Insert input
                    self.progress = ' '.join(temp)  # Rejoin the progress string
        else:
            print('The word dose not contain that character !!!')
            self.guesses -= 1

    def play(self):
        '''Function that plays the game'''
        Win = True
        while self.progress.replace(' ','') != self.word:
            self.display()
            user_guess = input('Make a guess: ')

            if user_guess == self.word:
                break

            if self.check_inp(user_guess): # Returns ture if the input is not a single character
                continue

            self.make_guess(user_guess)
            if self.guesses == 0:
                Win = False
                break

        if Win:
            print('You did it congratulations !!!\n\n')
            return True
        else:
            print('Ooo No you hanged the poor fella !!!\n\n')
            return False

def loading_screen():
    '''Code that playes the game'''
    score = 0
    while True:
        print('======================\n' + 'Welcome to Hangman.exe\n' + '======================\n')
        print('Your current score: ' + str(score) + '\n')
        print('1: Play\n' + '2: Set Guesses\n' + '3: Add Word to Bank\n' + '4: Quit')
        user_inp = input('Enter in a number: ')

        random_word = pick_word()

        if user_inp == '1':
            Hangman = Game(random_word)
            if Hangman.play():
                score += 1

        if user_inp == '2':
            user_int = input('Enter in amont of guesses alowed: ')
            Hangman = Game(random_word, int(user_int))
            if Hangman.play():
                score += 1

        if user_inp == '3':
            user_str = input('Enter in a word to add to the Bank: ')
            add_word(user_str)

        if user_inp == '4':
            break

def pick_word():
    '''Picks and returns a word from the word bank'''
    file_open = open('word_bank.txt','r')
    words_list = []
    for line in file_open:
        words_list.append(line.strip())
    file_open.close()
    return random.choice(words_list)

def add_word(inp_str):
    '''Adds given string to the word bank'''
    inp_str = inp_str.lower()
    inp_str += '\n'

    file_open = open('word_bank.txt','a+')
    file_open.write(inp_str)
    file_open.close()


if __name__ == "__main__":
    loading_screen()
