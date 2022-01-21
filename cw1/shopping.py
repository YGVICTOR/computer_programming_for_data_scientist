import json
import re
from datetime import date


class Product:
    def __init__(self,name,price,product_id,quantity,brand):
        self.__name = name
        self.__price = price
        self.__product_id = product_id
        self.__quantity = quantity
        self.__brand = brand

    def set_name(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def set_price(self,price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    def set_quantity(self,new_quantity):
        self.__quantity = new_quantity

    @property
    def quantity(self):
        return self.__quantity

    def set_product_id(self,product_id):
        self.__product_id = product_id

    @property
    def product_id(self):
        return self.__product_id;

    def set_brand(self,brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def to_json(self):
        attribute_dict = {}
        attribute_dict["name"] = self.__name
        attribute_dict["price"] = self.__price
        attribute_dict["quantity"] = self.__quantity
        attribute_dict["product_id"]=self.__product_id
        attribute_dict["brand"] = self.__brand
        json_attribute = json.dumps(attribute_dict)
        return json_attribute


class Clothing(Product):
    def __init__(self,name,price,product_id,quantity,brand,size,material):
        super().__init__(name,price,product_id,quantity,brand)
        self.__size = size
        self.__material = material

    def set_size(self,size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def set_material(self,material):
        self.__material = material

    @property
    def material(self):
        return self.__material

    def to_json(self):
        json_attribute = super().to_json()
        attribute_dict = json.loads(json_attribute)
        attribute_dict["size"] = self.__size
        attribute_dict["material"] = self.__material
        json_attribute = json.dumps(attribute_dict)
        return json_attribute

    def get_class(self):
        return self.__class__.__name__


class Food(Product):
    def __init__(self,name,price,product_id,quantity,brand,expiry_date,gluten_free,suitable_for_vegans):
        super().__init__(name,price,product_id,quantity,brand)
        self.__expiry_date = expiry_date
        self.__gluten_free = gluten_free
        self.__suitable_for_vegans = suitable_for_vegans

    def set_expiry_date(self,expiry_date):
        self.__expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self.__expiry_date

    def set_gluten_free(self,gluten_free):
        self.__gluten_free = gluten_free

    @property
    def gluten_free(self):
        return self.__gluten_free

    def set_suitable_for_vegans(self,suitable_for_vegans):
        self.__suitable_for_vegans = suitable_for_vegans

    @property
    def suitable_for_vegans(self):
        return self.__suitable_for_vegans

    def to_json(self):
        json_attribute = super().to_json()
        attribute_dict = json.loads(json_attribute)
        attribute_dict['expiry_date'] = self.__expiry_date
        attribute_dict['gluten_free'] = self.__gluten_free
        attribute_dict['suitable_for_vegans'] = self.__suitable_for_vegans
        json_attribute = json.dumps(attribute_dict)
        return json_attribute

    def get_class(self):
        return self.__class__.__name__


class Book(Product):
    def __init__(self, name, price, product_id, quantity, brand, author, genre):
        super().__init__(name,price,product_id,quantity,brand)
        self.__author = author
        self.__type = genre

    def set_author(self,author):
        self.__author = author

    @property
    def author(self):
        return self.__author

    def set_type(self,type):
        self.__type = type

    @property
    def type(self):
        return self.__type

    def to_json(self):
        json_attribute = super().to_json()
        attribute_dict = json.loads(json_attribute)
        attribute_dict['author'] = self.__author
        attribute_dict['type'] = self.__type
        json_attribute = json.dumps(attribute_dict)
        return json_attribute

    def get_class(self):
        return self.__class__.__name__

class ShoppingCart:
    def __init__(self):
        self.__cart = list()

    def add_product(self,p):
        self.__cart.append(p)

    def remove_product(self,p):
        self.__cart.remove(p)

    def get_contents(self):
        self.__cart.sort(key=lambda x: x.name.upper())
        return self.__cart

    def change_product_quantity(self,p,q):
        index = self.__cart.index(p)
        self.__cart[index].set_quantity(q)

    def shopping_cart_to_json(self):
        normal_data = {}
        for product in self.get_contents():
            normal = json.loads(product.to_json())
            normal['product_class'] = product.get_class()
            normal_data[normal['product_id']] = normal
        json_data = json.dumps(normal_data, indent=4, separators=(',', ':'))
        return json_data


# helper function to ensure user input a positive(0 is also allowed) integer
def read_positive_integer(string_content):
    try:
        result = int(input(string_content))
        if result >= 0:
            return result
        else:
            print("your input is incorrect, please input a positive integer")
            return read_positive_integer(string_content)
    except:
        print("your input is incorrect, please input a positive integer")
        return read_positive_integer(string_content)


# helper function to ensure user input a positive number(0 is also allowed)
def read_positive_float(string_content):
    try:
        result = float(input(string_content))
        if result >= 0:
            return result
        else:
            print("your input is incorrect, please input a positive number")
            return read_positive_float(string_content)
    except:
        print("your input is incorrect, please input a positive number")
        return read_positive_float(string_content)


# helper function to ensure user input boolean(case insensitive: so both True and true are legal)
def read_boolean_value(string_content):
    try:
        result = input(string_content)
        if eval(result.capitalize()) == True or eval(result.capitalize()) == False:
            return eval(result.capitalize())
        else:
            print("your input is incorrect, please input True or False")
            return read_boolean_value(string_content)
    except:
        print("your input is incorrect, please input True or False")
        return read_boolean_value(string_content)


# check that ean code that user input is unique consisting of 13 digits.
def input_valid_ean_code(ean_code_dict):
    potential_ean_code = input("Insert its EAN code: ")
    pattern = "\d{13}"
    if re.search(pattern,potential_ean_code):
        if potential_ean_code not in ean_code_dict.keys():
            return potential_ean_code
        else:
            message = 'the EAN code you just input is duplicate with {}, please reinput it'.format(ean_code_dict[potential_ean_code])
            print(message)
            return input_valid_ean_code(ean_code_dict)
    else:
        print('EAN Code must be 13 digits, check your input format')
        return input_valid_ean_code(ean_code_dict)


# input a date and check if it is a legal date; format : yyyy-mm-dd
def date_input():
    date_string = input("Insert its expiry date: ")
    pattern = "\d{4}-\d{2}-\d{2}"
    if re.search(pattern,date_string):
        if check_date_valid(date_string):
            return date_string
        else:
            print('your date inputed is illegal, no such day on calendar please re input the correct date')
            return date_input()
    else:
        print('your input format is invalid, please check the input format: yyyy-mm-dd')
        date_input()

# check if it is a legal date; format : yyyy-mm-dd
def check_date_valid(datestr):
    try:
        date.fromisoformat(datestr)
    except:
        return False
    else:
        return True


if __name__ == '__main__':
    print('The program has started.')
    print('Insert your next command (H for help):')
    terminated = False
    shopping_cart = ShoppingCart()
    while not terminated:
        c = input("Type your next command:")
        if c.upper() == 'T':
            terminated = True
        elif c.upper() == "A":
            print("Adding a new product: ")
            type = input("Insert its type: ")
            type = type.capitalize()
            while type not in ["Clothing","Food","Book"]:
                print('sorry, at this point, we only support 3 different types:')
                print('Clothing, Food, Book')
                type = input("Please reinsert its type: ")
                type = type.capitalize()
            name = input("Insert its name: ")
            price_string_content = "Insert its price (£): "
            price = read_positive_float(price_string_content)
            string_content = "Insert its quantity: "
            qty = read_positive_integer(string_content)
            brand = input("Insert its brand: ")
            ean_code_dict = {}
            for product in shopping_cart.get_contents():
                ean_code_dict[product.product_id] = product.name
            product_id = input_valid_ean_code(ean_code_dict)
            if type == "Clothing":
                size = input("Insert its size: ")
                material = input("Insert its material: ")
                clothing = Clothing(name,price,product_id,qty,brand,size,material)
                shopping_cart.add_product(clothing)
                print("The product {} has been added to the cart".format(name))
                print("The cart contains {} products.".format(len(shopping_cart.get_contents())))

            elif type == "Food":
                expiry_date = date_input()
                boolean_information = "If it is gluten-free: (True/ False)"
                gluten_free = read_boolean_value(boolean_information)
                boolean_information = "If it is suitable for vegans: (True/False)"
                suitable_for_vegans = read_boolean_value(boolean_information)
                food = Food(name,price,product_id,qty,brand,expiry_date,gluten_free,suitable_for_vegans)
                shopping_cart.add_product(food)
                print("The product {} has been added to the cart".format(name))
                print("The cart contains {} products.".format(len(shopping_cart.get_contents())))

            elif type == "Book":
                author = input("Insert its author: ")
                genre = input("Insert its genre: ")
                book = Book(name, price, product_id, qty, brand, author, genre)
                shopping_cart.add_product(book)
                print("The product {} has been added to the cart".format(name))
                print("The cart contains {} products.".format(len(shopping_cart.get_contents())))

        elif c.upper() == 'H':
            print("The program supports the following commands:")
            print("    [A] - Add a new product to the cart")
            print("    [R] - Remove a product from the cart")
            print("    [S] - Print a summary of the cart")
            print("    [Q] - Change the quantity of a product")
            print("    [E] - Export a JSON version of the cart")
            print("    [T] - Terminate the program")
            print("    [H] - List the supported commands")

        elif c.upper() == "S":
            print("This is the total of the expenses:")
            total = 0
            cart = shopping_cart.get_contents()
            i = 1
            for item in cart:
                item_quantity = int(item.quantity)
                item_name = item.name
                price_per_item = float(item.price)
                price_items = item_quantity*price_per_item
                total += price_items
                if(item_quantity==1):
                    print("    {} - {} = £{}".format(i,item_name,price_items))
                else:
                    print("    {} - {} * {} = £{}".format(i,item_quantity,item_name,price_items))
                i += 1
            print("    Total = £{}".format(total))

        elif c.upper() == "E":
            if len(shopping_cart.get_contents()) == 0:
                print("Sorry, you haven't added any product in the shopping_cart")
            else:
                print(shopping_cart.shopping_cart_to_json())

        elif c.upper() == "R":
            if len(shopping_cart.get_contents()) == 0:
                print("Sorry, you haven't added any product in the shopping cart.")
            else:
                ean_code = input("please input the 13-digits ean code")
                ean_code_list = [item for item in shopping_cart.get_contents()]
                idx =[item for item in ean_code_list if item.product_id == ean_code]
                if len(idx) == 0:
                    print("Sorry, the ean code you have just input is incorrect")
                else:
                    shopping_cart.remove_product(idx[0])
                    print("you have successfully remove {} from your shopping cart".format(idx[0].name))

        elif c.upper() == "Q":
            if len(shopping_cart.get_contents()) == 0:
                print("Sorry, you haven't added any product in the shopping_cart")
            else:
                ean_code = input("please input the 13-digits ean code of the product that you want to change the quantity: ")
                ean_code_list = [item for item in shopping_cart.get_contents()]
                idx = [item for item in ean_code_list if item.product_id == ean_code]
                if len(idx) == 0:
                    print("Sorry, the ean code you have just input is incorrect")
                else:
                    string_contenet = "please input the quantity that you wish to change: "
                    qty = read_positive_integer(string_contenet)
                    shopping_cart.change_product_quantity(idx[0], qty)
                    print("you have changed the quantity to {} successfully".format(qty))
        else:
            print("Command not recognised. Please try again")
    print( 'Goodbye.')