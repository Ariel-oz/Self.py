def sequence_del(my_str):
    new_str = ""
    temp = ""
    for i in my_str:
        if str(i) != temp:
            new_str += str(i)
        temp = str(i)
    return new_str
print(sequence_del("Heeyyy   yyouuuu!!!"))
