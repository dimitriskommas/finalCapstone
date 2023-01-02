
from tabulate import tabulate
#========The beginning of the class==========
class Shoe:
    # The constructor will be created and initialize the 5 different attributes of the shoe instance
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # This method will return the cost of the shoe
    def get_cost(self):
        return int(self.cost)

    # This method will return the quantity of the shoe
    def get_quantity(self):
        return int(self.quantity)

    # This method will return the code of the shoe
    def get_code(self):
        return self.code
    
    # This method will update the quantity of the stock
    def update_quantity(self, restock):
        self.quantity = str(int(self.quantity) + restock)
        return
    
    # This method will return a string representation of the object
    def __str__(self):
        return f"Shoe details:\n country of origing: {self.country}\n code: {self.code}\n product: {self.product}\n cost: {self.cost}\n quantity: {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
 

'''
This function will open the file inventory.txt
and read the data from this file, then create a shoes object with this data
and append this object into the shoes list. One line in this file represents
data to create one object of shoes.
'''
def read_shoes_data():
    # Firstly, the function tries to open the inventory.txt file to read
    # if it doesn't exist it displays an error message and quits the program since there is no txt file to be used
    try:
        f = open("inventory.txt", 'r')
    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist")
        print(error)
        quit()

    # Then the first line is skipped so it starts reading the second line
    next(f)
    # The for loop will go through the file
    for line in f:
        # Each line will be splitted based on commas
        data = line.split(',')
        # The value of the first position will be passed to the country variable, the second to code variable and so on
        country = data[0]
        code = data[1]
        product = data[2]
        # The value of cost and quantity should be numerical, so the try-except will make sure a number is passed to the variable
        try:
            cost = int(data[3])
        except ValueError:
            print("There is a no valid cost in the file.")
            f.close()
            return
        # Because the value of the quantity is on the last, the strip method is used to remove the change of line
        # If the value is not numerical, an error message will be printed and the function will exit
        try:
            quantity = int(data[4].strip())
        except ValueError:
            print("There is a no valid quantity in the file.")
            f.close()
            return
        # Then all the variables will be used to create a new object of shoe and pass it to 
        shoe_list.append(Shoe(country, code, product, cost, quantity))    
    f.close()
    return

'''
This function will allow a user to capture data
about a shoe and use this data to create a shoe object
and append this object inside the shoe list.
The user's input will also be added to the inventory.txt file.
'''
def capture_shoes():
    # The function will ask the user to pass the values for each atttibute of the object.
    # It will make sure that there are going to be passed numerical values to tquantity and cost of the product
    country = input("Enter the country of origin og the shoe: ")
    code = input("Enter the code of the product: ")
    product = input("Enter the product name: ")
    while True:
        try:
            cost = int(input("Enter the cost of the product: "))
            break
        except ValueError:
            print("You passed a non numerical value, please try again.")

    while True:
        try:
            quantity = int(input("Enter the quantity of the stock for the specific product: "))
            break
        except ValueError:
            print("You passed a non numerical value, please try again.")
    
    # Then a new object will be created and passed to the shoe_list 
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    # Then the inventory file will also be updated with the new entry
    f = open("inventory.txt", 'a')
    f.write('\n' + country + ',' + code + ',' + product + ',' + str(cost) + ',' +  str(quantity))
    f.close()

'''
This function will read the file and display its data to a table
'''
def view_all():
    # Opens the file to read
    f = open("inventory.txt", 'r')
    # Create an empty list
    data = []
    # The for iterates the file's lines
    for line in f:
        # Each line will be splitted based on commas
        data.append(line.strip().split(','))
    
    # The file then it's closed
    f.close()

    # Prints the data list as a table
    print(tabulate(data, headers='firstrow', tablefmt='fancy_grid', showindex="always"))
    return

'''
This function will find the shoe object with the lowest quantity,
which is the shoes that need to be re-stocked. Ask the user if they
want to add this quantity of shoes and then update it.
This quantity should be updated on the file for this shoe.
'''
def re_stock():
    # To find the minimum value, the quantity of the first shoe is passed to min.
    min = shoe_list[0].get_quantity()
    # As the for will iterate the shoe_list, the position of the minimum will get changed
    # So it's initialized as 0 (the very first position)
    min_position = 0
    # The position variable will get increased as it checks the next element of the list
    # So when a new minimum value is found, its value will be passed to min_position
    position = 0
    # The for iterates the shoe_list
    for shoe in shoe_list:
        # if class the get_quantity method of the object to check if the quantity of the object is less than the minimum
        if shoe.get_quantity() < min:
            # If it's true the new minimum quantity will be passed to min
            # and the position of the object of the list will be passed to min_position
            min = shoe.get_quantity()
            min_position = position
        position += 1

    # Then the details of the shoe with the minimum stock gets printed
    print("The following shoe has the minimum stock")
    print(shoe_list[min_position])

    # The user will be asked then if the stock needs to be updated
    option = input("Would you like to update the stock? (yes/no) ")
    if option == "yes":
        # A string is created to store all the old a new data
        data = ""
        # The user will ba asked then, the restock quantity
        restock = int(input("what's the re-stock quantity? "))
        # The update_quantity will be called to update the stock in the shoe_list
        shoe_list[min_position].update_quantity(restock)
        # The inventory.txt will be opened and pass all its data to to string it was created earlier
        f = open("inventory.txt", 'r')
        # To pass the updated value of the stock, the line number will be tracked with line_number
        line_number = 0
        for line in f:
            # As for goes through each line, the line_number will be compared with minimum position
            # Because the shoe_list was used to find the minimum position, the first line of the file is not included
            # So to make sure the shoe with the minimum value is found, the minim_mum position should be increased by one
            if line_number == min_position+1:
                # When the shoe with the minimum stock is found, the data of the line will be splited based on ','
                # and pass again to the line as a list
                line = line.split(',')
                # The quantity is calculated and passed to the last position of the new list
                total_quantity = min + restock
                line[-1] = str(total_quantity)
                # Then the elements of list are joined back together with ','
                line = ','.join(line)
                # Finally the new line is passed to the data string with a change of line at the end
                data += line + "\n"
            else:
                # If it's not the minimum, the line is just passed to the data string
                data += line
            
            # The line number gets increased by 1 to be compared with the minimum position 
            line_number += 1
        
        # Then the file is closed
        f.close()
    
    # The file will be opened again to write the data string with the updated stock and then will close
    f = open("inventory.txt", 'w+')
    f.write(data)
    f.close()

'''
This function will search for a shoe from the list
using the shoe code and return this object so that it will be printed.
'''
def search_shoe():
    # The function asks the user to pass the code
    search_code = input("Enter the code of the shoe you are looking for: ")

    # If the code is found in the list, the shoe details are printed and return is used to exit the function
    for shoe in shoe_list:
        if search_code == shoe.get_code():
            print(shoe)
            return
    
    # If the code wasn't found, a message is printed to let the user know
    print("The product with this code wasn't found.")

    return 

'''
This function will calculate the total value for each item.
Please keep the formula for value in mind: value = cost * quantity.
Print this information on the console for all the shoes as a table.
'''
def value_per_item():
    # Opens the file to read
    f = open("inventory.txt", 'r')
    # Creates an empty list
    data = []
    # The boolean variable first_line is initialized as True and it will be used to make sure the first entry to the list is modified
    first_line = True
    # The for goes throught the file
    for line in f:
        # If it reads the first line
        if first_line == True:
            # It splits the line based on ','
            # The method strip() is used to remove any \n
            list_line = line.strip().split(',')
            # the string Stock Value needs to be appended to the first entry, since it will be used as the headers of the table
            list_line.append("Stock Value")
            # Then the list will be passed to the data list
            data.append(list_line)
            # The boolean then sets to False
            first_line = False
        else:
            # If it's not the first line, after the line gets splitted based on commas
            list_line = line.split(',')
            # Then passes the total value of the stock by multiplying the last two elements of the newly created list (stock*cost)
            list_line.append(str((int(list_line[-1])*int(list_line[-2]))))
            # Then the list will be passed to the data list
            data.append(list_line)
    
    # The file then is closed
    f.close()
    # Then the data will be presented as a table
    print(tabulate(data, headers='firstrow', tablefmt='fancy_grid', showindex="always"))
    return
     

'''
Write code to determine the product with the highest quantity and
print this shoe as being for sale.
'''
def highest_qty():
    # The max value is initialized to the quantity of the first shoe in the list
    max = shoe_list[0].get_quantity()
    # Then the position of the max value is initialized to 0
    # the position variable will keep track of the position of the element that will be checked in the for loop
    max_position = position = 0
    for shoe in shoe_list:
        # If the shoe quantity is greater than the max
        if shoe.get_quantity() > max:
            # The max value will change
            max = shoe.get_quantity()
            # And the current position will be passed to the max position
            max_position = position
        # At the end of each loop the position will be increased by one
        position += 1

    # Then the function will display the max value and the shoe that needs to be on sale to the user
    print("The following shoe has the highest stock ({max}) and needs to be on sale")
    print(shoe_list[max_position])

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# The function read_shoes_data is called so the data to the shoe_list are created
read_shoes_data()

# The user_choice will store the user's option each time
user_choice = ""

# The loop makes sure will continue to ask the user until he/she decide to quit
while user_choice != "quit":
    # The program asks from the user to pass an option
    user_choice = input("What would you like to do - new entry/view stock/restock/search/value/sale/quit? ")

    # If the user asks to for new entry, the capture_shoes function is being called
    if user_choice == "new entry":
        capture_shoes()
    
    # If the user asks to view_stock, the view_all function will be called 
    # and all the available stock will be printed to the user as a table
    elif user_choice == "view stock":
        view_all()

    # If the user ask to restock a product, the re_stock function is being called
    # the user will be asked if he wants to restock the product with the smallest stock
    elif user_choice == "restock":
        re_stock()

    # If the user chooses to search, the search_shoe function will be called.
    # The user will be asked for a product code and the function will print the information about it
    elif user_choice == "search":
        search_shoe()

    # If the user asks the value option, the value_per_item table will be called
    # and the available stock will be printed with an extra column with the total value of each product
    elif user_choice == "value":
        value_per_item()


    # If the user chooses the sale option, the highest_qty function will be called
    # and the program will print the product with the highest stock that needs to be on sale      
    elif user_choice == "sale":
        highest_qty()

    # If the user asks to quit the program will terminate
    elif user_choice == "quit":
        print("Goodbye")
    # Otherwise it will ask again for a valid input
    else:
        print("Oops - incorrect input")