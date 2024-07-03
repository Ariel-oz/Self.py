product = input("enter list of products: ").split(",")
chose_user = int(input("enter an option 1-9: "))

while chose_user != 9:
    if chose_user == 1:
         print(product)
    elif chose_user == 2:
         print(len(product))
    elif chose_user == 3:
        prod = input("enter a product: ")
        if prod in product:
            print("its on the list")
        else:
            print("not on the list")
    elif chose_user == 4:
        prod = input("enter a product: ")
        print(product.count(prod))
    elif chose_user == 5:
        new_list = product
        user_input = input("enter a product: ")
        new_list.remove(user_input)
        print(new_list)
    elif chose_user == 6:
        new_list = product
        user_input = input("enter a product: ")
        new_list.append(user_input)
        print(new_list)
    elif chose_user == 7:
        new_lst = []
        for i in product:
            if len(i) < 3 or not i.isalpha():
                new_lst.append(i)
        print(new_lst)
    elif chose_user == 8:
        product = list(set(product))
    chose_user = int(input("enter an option 1-9: "))

    



    
