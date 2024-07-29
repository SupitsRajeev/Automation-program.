
# importing the libraries
import read
import write
import operations

print("\n")
print("-----------------------------------------------")
print("| \t\t Welcome To The MUDITA STORE \t\t |")
print("|           KAlANKI,Kathmandu14")
print("------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t")

loop = True
while loop:
    key_dictionary = read.read_file()

    print("Press 1 to Sell the Laptops.")
    print("Press 2 to Purchase the Laptops.")
    print("Press 3 to Exit from the Shop.")

    user_input = int(input("Enter your choice: "))

    print("\n")

    if user_input == 1:
        print("-------------------------------------------------------")
        print("Please provide your details to generate the bill")
        print("-------------------------------------------------------")
        print("\n")

        name = input("Please enter your name: ")
        print("\n")

        phone_number = input("Please enter your phone number: ")
        print("\n")


        Buy_more = True

        while Buy_more:
            print("SN \t Product Name \t  Company \t Price \t Quantity \n")
            with open("laptop.txt", "r") as f:
                a = 1
                for line in f:
                    print(a, "\t\t" + line.replace(",", "\t"))
                    print(
                        "----------------------------------------------------------------------------")
                    a += 1

            
            laptop_sold_by_user = operations.Sell_laptops(key_dictionary, name)
            write.updatelaptop(key_dictionary) 
            write.bill_generation(key_dictionary, laptop_sold_by_user)
            print("\n")
            break

    elif user_input == 2:
        print("-------------------------------------------------------")
        print("Please provide your details to generate the bill")
        print("-------------------------------------------------------")
        print("\n")

        name = input("Please enter your name: ")
        print("\n")

        phone_number = input("Please enter your phone number: ")
        print("\n")

        print(
            "----------------------------------------------------------------------------")
        print("\n")

        
        Sell_more = True

        while Sell_more:
            print("SN \t Product Name \t  Company \t Price \t Quantity \n")
            with open("laptop.txt", "r") as f:
                a = 1
                for line in f:
                    print("--------------------------------------------------------------------------")
                    print(a, "\t\t" + line.replace(",", "\t"))
                    print(
                        "----------------------------------------------------------------------------")
                    a += 1

            laptop_bought_by_user = operations.buy_laptops(key_dictionary, name)
            write.updatelaptop(key_dictionary)
            write.bills_boughtlaptops(key_dictionary, laptop_bought_by_user)
            print("\n")
            break

    elif user_input == 3:
        print("Thank you for visiting our shop")
        break

    else:

        print("Invalid option. Please enter a number between 1 and 3.")

