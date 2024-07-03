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

{MAX_TRIES}
 """)

user_input_tav= input("Guess a word:")
input_len = len(user_input_tav)
int(input_len)
print ( "_ " * input_len)
if (input_len > 1) and (user_input_tav.isalpha() == "false"):
    print ("E3")
elif (user_input_tav.isalpha() == "false"):
    print("E2")
elif (input_len > 1 ):
    print("E1")
else:
    print(user_input_tav.lower())




