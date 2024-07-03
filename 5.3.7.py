def chocolate_maker(small, big, x):

    """this function calculate if the choclate cubes fits the length that entered"""
    
    #set the cubes
    choc_s = int(small) 
    choc_b = int(big) * 5

    # checkes if sum of cubes lower than x
    if choc_s + choc_b < x:
        return False

    # checks if sum of cubes equals x
    if choc_s + choc_b == x:
        return True

    # if there isn't small cubes, x must be divided by 5 without sherit
    if choc_s == 0:
        return (x % 5 == 0)

    # if there isn't big cubes and we know that sum is higher than x
    if choc_b == 0:
        return True
    
    #if x % choc_s + choc_b != 0:
    #    return True

    # if x is divided by 5 and we have enought big cubes
    if x % 5 == 0 and choc_b >= x:
        return True

    if choc_b + choc_s >= x:
        return True
        

    
print(help(chocolate_maker))
    
        
        

user_input = print("please provide how much small choclate cube, how much big choclate cube and the length: ")
lst = []
for i in range(0,3):
    lst.append(int(input()))
    

print(chocolate_maker(small=lst[0], big=lst[1], x=lst[2]))
