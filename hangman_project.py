from random import randint

guess_number=randint(1,7)
MAX_TRIES = 6

print(f"""
Welcome to the game Hangman
                                       
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/

your maximum tries are: {MAX_TRIES}
 """)

user_input_tav= input("Guess a letter:")
if not user_input_tav.isalpha() == True:
    print("The input is not valid")

def is_valid_input(letter_guessed):
    """ check if the user input is a valid char"""
    if len(letter_guessed) >= 2:
    #check if input is only one char
        return False
    # check if the char is alpanumeric 
    return letter_guessed.isalpha()
  
        

print(is_valid_input(user_input_tav))

input()