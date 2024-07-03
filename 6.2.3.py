def format_list(my_list):
    """ the func will return only the srings in the zugi place and the last string"""
    zugi = ''.join(my_list[:-1:2])
    last_str = ''.join(my_list[-1])
    return zugi + " and " + last_str


user_inp = input("get list of strings")
lst = user_inp.split(',')

if len(lst) % 2 != 0:
    print("not zugi")
else:
    print (format_list(lst))
    
