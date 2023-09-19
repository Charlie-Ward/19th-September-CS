def max_int(list_int):
    global max_number
    max_number = list_int[0]
    for i in range(1, len(list_int) - 1):
        if list_int[i] > max_number:
            max_number = list_int[i]
    return max_number


listInt = []
max_int(listInt)
print(max_number)