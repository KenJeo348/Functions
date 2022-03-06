def number_in_list(list, multiple):
    new_list = []
    for num in list:
        if num % multiple == 0:
            new_list.append(num)
    return  new_list


# Main Routine
list_ = [1, 4, 6, 7, 15, 22, 35]

print(number_in_list(list_, 5))
print(number_in_list(list_, 2))
