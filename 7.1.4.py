
def squared_numbers(start, stop):
    start = int(start)
    stop = int(stop)
    x = []
    while start <= stop:
        x.append(start ** 2)
        start += 1
    return x

start = input("enter number start: ")
stop = input("enter number stop: ")

print(squared_numbers(start,stop))

