class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
    def describe_shop(self):
        print(f"{self.shop_name} це {self.store_type} магазин.")
    def open_shop(self):
        print("The shop is open!")
    def set_number_of_units(self, number):
        self.number_of_units = number 
    def increment_number_of_units(self, increment):
        self.number_of_units += increment
store1 = Shop("Магазин№1","продуктовий" )
print(store1.shop_name)
print(store1.store_type)
store1.describe_shop()
store2 = Shop("Магазин№2","продуктовий")
store2.describe_shop()
store3 = Shop("Магазин№3","продуктовий")
store3.describe_shop()
store4 = Shop("Магазин№4","продуктовий")
store4.describe_shop()
store1.set_number_of_units(30)
print(store1.number_of_units)
store1.increment_number_of_units(30)
print(store1.number_of_units)     

class Discount(Shop):
     def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products
     def get_discount_products(self):
        print("Discount products:")
        for product in self.discount_products:
            print(product)
store_discount = Discount("Знижки", "Продуктовий", ["Хліб", "Огірок", "Квас"])
store_discount.get_discount_products()

class User:
    def __init__(self, first_name,second_name, last_visit, rating):
       self.first_name = first_name
       self.second_name = second_name
       self.last_visit = last_visit
       self.rating = rating
       self.login_attempts = 0
    def describe_user(self):
         print(f"{self.first_name} {self.second_name}")
    def greeting_user(self):
         print(f" Hello {self.first_name} {self.second_name}")    
    def increment_login_attempts(self):
        self.login_attempts += 1      
    def reset_login_attempts(self):
        self.login_attempts = 0    
class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
class Admin(User):
    def __init__(self, first_name, last_name,last_visit, rating ):
        super().__init__(first_name, last_name, last_visit, rating)
        self.privileges = Privileges()
    def show_privileges(self):
        self.privileges.show_privileges()
