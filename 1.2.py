msg = input("enter a str")
if len(msg) >= 2:
  msg1 = msg[1:].replace(msg[0],"e")
  msg2 = msg[0:1] + msg1
  print(msg2)
else:
  print(msg)
