def main_routine():
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
    while ticket_wanted == "Y":
        ticket = sell_ticket()

        num_tickets = int(input("How many of these tickets do you want:"))
        confirm = input(f"Confirm purchase of {num_tickets} type {ticket}"
                        f"ticket(s? (Y/N): ").upper()
        if confirm == "Y":
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
        elif ticket == "S":
            student_tickets += num_tickets
        elif ticket == "C":
            child_tickets += num_tickets
        else:
            ticket_wanted = input("Do you want to sell"
                                  "another ticket? (Y/N): ").upper()
    print("==================================================")
    print(f"The total tickets sold today was {tickets_sold}/n"
          f"This was made up of: "
          f"{adult_tickets} for adults;"
          f"{student_tickets} for students;"
          f"{child_tickets} for children;"
          f"{gift_tickets} gift vouchers")
    print(f"Sales for the day came to ${total_sales:.2f}")
    print("==================================================")


def sell_ticket():
    ticket_type = input("What kind of ticket do you want: "
                        "A for Adult,"
                        "S for Student,"
                        "C for Child,"
                        "G for Gift voucher"
                        ">>").upper()
    return ticket_type


def get_price(type_):
    prices = [["A", 12.5], ["S", 9], ["C", 7], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Main Routine
print("***************** Fan fare Movies - ticketing system ********************/n")
main_routine()
