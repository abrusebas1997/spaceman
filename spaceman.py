import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r') #r keep the file open
    words_list = f.readlines() #f.readlines is reading all the words in my word.txt
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word



def is_word_guessed(secret_word, guessed_letters):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    allcorrect = True
    for letter in secret_word:
        if letter not in guessed_letters:
            allcorrect = False
    return allcorrect
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    #pass

def get_guessed_word(secret_word, guessed_letters):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    answers_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            answers_word += letter+' '
        else:
            answers_word += "_ "
    return answers_word


    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    #pass
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    #
    if guess in secret_word:
        return True
    else:
        return False

def is_guess_in_letters(guess, guessed_letters):
    '''
    A function to check if the guess is e letters
    '''
    if guess in guessed_letters:
        return True
    else:
        return False

def play_again():

    play_again = False
    answer = input('Game is over, would you like to play again? (Y/N)')
    if answer == 'Y' or 'yes':
        play_again = True
    else:
        quit()




def spaceman(secret_word):
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    guessed_letters = [ ]
    guesses_left = 7
    alphabet = list("abcdefghijklmnopqrstuvwxyz")


    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec
    print(f"Welcome to Spaceman!\n The Secret word contains {len(secret_word)} letters")
    print("You have 7 incorrect guesses, please enter one word per round" )
    show_me = get_guessed_word(secret_word, guessed_letters)
    print(show_me)


    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while is_word_guessed(secret_word, guessed_letters) == False:
        guess = input("Enter one letter: ")
        #If the input is more than one letter, it's going to be wrong
        if len(guess) != 1:
            print("Please just enter one letter")
        #If the input is not a letter it's going to be False, thus wrong
        elif guess.isalpha() == False:
            print("Sorry your guess was not a letter, try again")
        #If you enter the same letter you used already
        elif is_guess_in_letters(guess, guessed_letters) == True:
            print("You enter this letter already")
        else:
            guessed_letters.append(guess)
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
            letter_inside_secret_word = is_guess_in_word(guess, secret_word)
            if letter_inside_secret_word == True:
                print("The letter you guess is correct")
            else:
                guesses_left -= 1
                print("The letter you guess is not correct")
                #TODO: show the guessed word so far
                print("Letters guessed so far", guessed_letters)
                alphabet.remove(guess)
                print("letters remaining:", "".join(alphabet))
                #TODO: check if the game has been won or lost
                if guesses_left == 0:
                    print("YOU LOST")
                    print(guesses_left)
                    play_again()
            show_me = get_guessed_word(secret_word, guessed_letters)
            print(show_me)
            print(guesses_left)
    if is_word_guessed(secret_word, guessed_letters) == True:
        print("YOU WIN")
        play_again()



#These function calls that will start the games
secret_word = load_word()
spaceman(secret_word)
