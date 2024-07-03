def numbers_letters_count(my_str):
    new_str = []
    num = 0
    letter = 0
    for element in my_str:
        if element.isnumeric():
            num += 1
        else:
            letter += 1
    return [num, letter]
        

userinput = input("enter string: ")
print(numbers_letters_count(userinput))
