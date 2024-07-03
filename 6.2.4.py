def extend_list_x(list_x, list_y):
    joined_list = [*list_x, *list_y]  # unpack both iterables in a list literal
    return joined_list



list_x = []
list_y = []

list_x = input("enter l1: ")
list_y = input("enter l2: ")
print(extend_list_x(list_x,list_y))
