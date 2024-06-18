my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
first = 0
while len(my_list) < 14:
    if my_list[first] > 0:
        print(my_list[first])
    elif my_list[first] == 0:
        pass
    elif my_list[first] < 0:
        break
    first += 1
