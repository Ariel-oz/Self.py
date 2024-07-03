#input client
#convert from c to f
temp = input("Insert the temperature you would like to convert: ")
if temp[-1] == "c" or temp[-1] == "C":
   temp_f = (9 * int(temp[:-1]) + 32 * 5) / 5
   print (str(temp_f) + "F")
elif temp[-1] == "f" or temp[-1] == "F":
    temp_c=(5* int(temp[:-1]) -160) / 9
    print (str(temp_c) + "C")
