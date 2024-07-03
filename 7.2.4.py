def seven_boom(end_number):
    result = []
    for num in range(0,end_number+1):
        if '7' in str(num)or num % 7 == 0:
            result.append("BOOM")
        else:
            result.append(num)
    return result

print(seven_boom(17))
