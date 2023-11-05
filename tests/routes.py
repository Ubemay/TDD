from models import Product  


def read_product_by_id(product_id):
    return Product.get_by_id(product_id)

def update_product(product_id, updated_data):
    product = Product.get_by_id(product_id)
    if product:
        product.update(updated_data)
        return product
    return None

def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if product:
        product.delete()
        return True
    return False

def list_all_products():
    return Product.get_all()

def find_product_by_name(name):
    return Product.find_by_name(name)

