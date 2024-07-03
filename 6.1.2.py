
def shift_left(my_list):
    fst= my_list[0]
    rest_of_lst = my_list[1:]
    new_lst = lst
    new_lst[:-1] = rest_of_lst
    new_lst[-1] = fst
    return new_lst

# idan's solution
def idan_shift_left(my_list):
    return my_list[1:] + [my_list[0]]

usr_inp = input("enter a list with 3 objects: ")
lst = usr_inp.split(',')

if len(lst) != 3:
    print("False")
else:
   print(shift_left(lst))
