import datetime as datentime


def updatelaptop(key_dictionary):
    with open("laptop.txt", "w") as f:
        for value in key_dictionary.values():
            f.write(value[0] + "," + value[1] + "," +
                    str(value[2]) + "," + str(value[3]) + "\n")

        return key_dictionary


def bill_generation(key_dictionary, laptop_sold_by_user):

    while True:
        # taking first name as input from user
        Name = input("Enter your customer name: ")
        # taking second name as input from user
        Phonenumber = input("Enter your customer phone number: ")
        current_date = datentime.datetime.now().strftime("%Y-%m-%d")


        bill_sold = f"Name of Customer: {Name}\n"
        bill_sold += f"Phone Number: {Phonenumber}\n"
        bill_sold += "-" * 100 + "\n"
        bill_sold += "\tProduct Name \t Price \t Quantity \t Total \n"
        bill_sold += "-" * 100 + "\n"
  
        total = 0
        for user_id, quantity_of_laptop in laptop_sold_by_user.items():
            name = key_dictionary[user_id][1]
            price = key_dictionary[user_id][2]
            total += int(price) * int(quantity_of_laptop)
            bill_sold += f"{name} \t\t {price} \t\t {quantity_of_laptop} \t\t {total} \n"
            bill_sold += "-" * 100 + "\n"

        Shipping = 500
        bill_sold += "-" * 100 + "\n"
        Grand_Total = total + Shipping

        bill_sold += "\n\nShipping: \t" + \
            str(Shipping) + "\nGrand Total: \t" + str(Grand_Total) + "\n"
        bill_sold += "-" * 100 + "\n"

        file_name = f"{Name}_{current_date}.txt"
        with open(file_name, "w") as f:
            f.write(bill_sold)

        print(bill_sold)


def bills_boughtlaptops(key_dictionary, laptop_bought_by_user):

    while True:
        # taking first name as input from user
        Name = input("Enter your customer name: ")
        # taking second name as input from user
        Phonenumber = input("Enter your customer phone number: ")
        current_date = datentime.datetime.now().strftime("%Y-%m-%d")

        # locating sell record text file
        
        bill_bought= f"Name of Customer: {Name}" + "\n"
        bill_bought += f"Phone Number of Customer: {Phonenumber}" + "\n"
        bill_bought += "Product Name \t\t Price \t\t Quantity \t\t Total \n"
        bill_bought += "-" * 100 + "\n"

        total = 0
        for user_id, quantity_of_laptop in laptop_bought_by_user.items():
            name = key_dictionary[user_id][1]
            price = key_dictionary[user_id][2]
            total += int(price) * int(quantity_of_laptop)
            bill_bought += name + "\t\t" + \
                str(price) + "\t\t" + str(quantity_of_laptop) + \
                "\t\t" + str(total) + "\n"
            bill_bought += "-" * 100 + "\n"

        VAT = 0.13 * total
        Grand_total = total + VAT
        bill_bought += "\n\n\n VAT: \t\t" + \
            str(VAT) + "\n Grand Total: \t\t" + str(Grand_total) + "\n"

        with open(f"{Name}_{current_date}.txt", "w") as f:
            f.write(bill_bought)

        print(bill_bought)
