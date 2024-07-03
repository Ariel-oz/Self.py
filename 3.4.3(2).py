client_inp = input ("enter a string: ")
len_str = len(client_inp)
mdl_str = len_str // 2 + 1
new_str = client_inp[mdl_str :]
new_str = new_str.upper()
client_output = (client_inp[:mdl_str]+new_str)
print (client_output)
