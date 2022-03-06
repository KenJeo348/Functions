def print_name(name, number):
    for item in range(0, number):
        print(name)


# Main Routine
enter_name = input("Enter a name: ")
enter_number = int(input("Enter a number: "))
print(print_name(enter_name, enter_number))
