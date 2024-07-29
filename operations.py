def buy_laptops(key_dictionary, name):
    laptop_bought_by_user = {}

    while True:
        try:
            # user id
            user_id = int(
                input("Please provide the ID of the laptop you would like to buy: "))
            print("\n")

            # valid user id
            while user_id <= 0 or user_id > len(key_dictionary):
                print("Your ID is invalid. Please enter the correct ID")
                print("\n")
                user_id = int(
                    input("Please provide the ID of the laptop you would like to buy: "))
                print("\n")

            # ask for the quantity of laptop
            quantity_of_laptop = int(
                input("Please provide the quantity of the laptop you would like to buy: "))

            # validating the quantity of laptop
            get_quantity_of_laptop = key_dictionary[user_id][3]

            if quantity_of_laptop <= 0 or quantity_of_laptop > int(get_quantity_of_laptop):
                print(
                    f"Sorry {name}! We don't have enough quantity of this laptop")
                print("\n")
                quantity_of_laptop = int(
                    input("Please provide the quantity of the laptop you would like to buy: "))
                print("\n"  )
 
           
            laptop_bought_by_user[user_id] = quantity_of_laptop

            # updating the quantity of laptop in dictionary
            key_dictionary[user_id][3] = int(
                get_quantity_of_laptop) + quantity_of_laptop
            while True:
                # asking if user wants to buy more
                buy_more = input("Do you want to buy more? (Y/N): ")
                print("\n")

                if buy_more == "Y" or buy_more == "y":
                    break
                elif buy_more == "N" or buy_more == "n":
                    return laptop_bought_by_user
        except ValueError:
            print("Please enter a valid input")
            print("\n")
            continue



def Sell_laptops(key_dictionary, name):
   
    laptop_sold_by_user = {}

    while True:
        try:
            # user id
            user_id = int(
                input("Please provide the ID of the laptop you would like to buy: "))
            print("\n")

            # valid user id
            while user_id <= 0 or user_id > len(key_dictionary):
                print("Your ID is invalid. Please enter the correct ID")
                print("\n")
                user_id = int(
                    input("Please provide the ID of the laptop you would like to buy: "))
                print("\n")

            # ask for the quantity of laptop
            quantity_of_laptop = int(
                input("Please provide the quantity of the laptop you would like to buy: "))

            # validating the quantity of laptop
            get_quantity_of_laptop = key_dictionary[user_id][3]

            while quantity_of_laptop <= 0 or quantity_of_laptop > int(get_quantity_of_laptop):
                print(
                    f"Sorry {name}! We don't have enough quantity of this laptop")
                print("\n")
                quantity_of_laptop = int(
                    input("Please provide the quantity of the laptop you would like to buy: "))
                print("\n")
 
           
            laptop_sold_by_user[user_id] = quantity_of_laptop

            # updating the quantity of laptop in dictionary
            key_dictionary[user_id][3] = int(
                get_quantity_of_laptop) - quantity_of_laptop
            while True:
                # asking if user wants to buy more
                Sell_more = input("Do you want to buy more? (Y/N): ")
                print("\n")

                if Sell_more == "Y" or Sell_more == "y":
                    break
                elif Sell_more == "N" or Sell_more == "n":
                    return laptop_sold_by_user
        except ValueError:
            print("Please enter a valid input")
            print("\n")
            continue
        
