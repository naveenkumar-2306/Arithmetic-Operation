from abc import ABC,abstractmethod

class AbstractProducts(ABC):
	def __init__(self):
		print("Abstract Class")
		
	@abstractmethod
	def get_name(self):
		raise NotImplementedError("Subclass must implemet this abstract method")
		
	@abstractmethod
	def display(self):
		raise NotImplementedError("Subclass must implemet this abstract method")	
		
class Product(AbstractProducts):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price
	
    def display(self):
    	print("I am in parent class Product")

class Electronic_Products(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_weight(self):
        return self._weight

class ShoppingCart:
    def __init__(self):
        self._cart_items = []

    def add_to_cart(self, product, quantity=1):
    	for i in range(quantity):
        	self._cart_items.append({'product': product, 'quantity': quantity})  ##Upload it as dictionary

    def remove_from_cart(self, product_name,quantity=1):
        for item in self._cart_items:
            '''print(product_name)
            print(type(product_name))
            print(item['product'].get_name())
            print(item['product'].get_name() == product_name)'''
            if item['product'].get_name() == product_name:
                self._cart_items.remove(item)
                print("Product Removed")
            else:
            	print("Break else")
            	break
            

    def calculate_total_cost(self):
        total_cost = 0
        for item in self._cart_items:
            total_cost += item['product'].get_price() 
        return total_cost


# Sample usage of the online shopping application
if __name__ == "__main__":
    # Create products
    Apple = Electronic_Products("Apple", 1000)
    
    Samsung = Electronic_Products("Samsung",2000)

    # Create shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_to_cart(Apple, 1)
    
    cart.add_to_cart(Samsung, 2)
    
    cart.remove_from_cart("Apple")
    
   #    cart.remove_from_cart("Samsung")
    
    cart.remove_from_cart("Samsung")
      
    price = cart.calculate_total_cost()
    
    print("Total Shopping_Cart Price : ",price)
    
    
    

