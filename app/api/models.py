from api.validation import *


products = []
sales = []

class Products():
    """
    This class deals with all the product's manipulations
    """ 
    def get_all_products(self):
        """
        This method is used by the admin to view all the products in store
        """
        if len(products) == 0:
            return "It's lonely here. There are no products yet"
        return products
    
    def get_product(self, id):
        """
        This method is used to fetch a specific product given the product's id
        """
        if valid_id(id) != "Valid":
            return valid_id(id)
        if len(products) == 0:
            return "It's lonely here. There are no products yet"
        prod = [x for x in products if x["id"] == id]
        if len(prod) == 0:
            return "Product with id {} not found. put a valid id".format(id)
        return prod[0]

    def add_product(self, name, price, qty_available, min_qty_allowed, category):
        """
        This hemethod is used by the admin to add a product in the store
        """
        if valid_name(name) != "Valid":
            return valid_name(name)
        if valid_price(price) != "Valid":
            return valid_price(price)
        if valid_quantity(qty_available) != "Valid":
            return valid_quantity(qty_available)
        if valid_quantity(min_qty_allowed) != "Valid":
            return valid_quantity(min_qty_allowed)
        if min_qty_allowed > qty_available:
            return "Minimum qty can't be greater than the qty available in store"
        if valid_category(category) != "Valid":
            return valid_category(category)
        prod = [x for x in products if x["name"] == name]
        if len(prod) != 0:
            return "Product with name {} already exists. Choose another name".format(name)
        id = len(products) + 1
        product = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": qty_available,
            "min_quantity": min_qty_allowed,
            "category": category
        }
        products.append(product)
        return "Successfully added product"

class SaleOrder():
    """
    This class deals with all sale's trafics
    """
    def add_sale_order(self, prod_id, quantity, attendant_name):
        """
        This method is used by the store attendant to add a sale order
        """
        if valid_id(prod_id) != "Valid":
            return valid_id(prod_id)
        if valid_quantity(quantity) != "Valid":
            return valid_quantity(quantity)
        if valid_name(attendant_name) != "Valid":
            return valid_name(attendant_name)
        if len(products) == 0:
            return "Empty store. There are no products in store yet"
        prod = [x for x in products if x["id"] == prod_id]
        if len(prod) == 0:
            return "Product with id {} was not found in store. Please put a valid one".format(prod_id)
        qty = prod[0]["quantity"]
        if quantity > qty:
            return "Invalid quantity. Qty ordered must be less than {}(qty in store)".format(qty)
        price = prod[0]["price"]
        id = len(sales) + 1
        total = price * quantity
        order = {
            "id": id,
            "product_id": prod_id,
            "price": price,
            "quantity": quantity,
            "total": total,
            "at_name": attendant_name
        }
        sales.append(order)
        return "Successfully added sale order"

    def get_all_sales(self):
        """
        This allows the admin user to ftch all the sale order records
        """
        if len(sales) == 0:
            return "The are no sale orders made yet"
        return sales
    