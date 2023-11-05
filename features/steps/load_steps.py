from behave import given
from service.routes import create_product  

@given('a product exists in the system')
def a_product_exists_in_system(context):
    product_data = {
        'name': 'Sample Product',
        'description': 'This is a sample product description.',
        'price': 20.0,
        'category': 'Sample Category',
        'availability': 'In stock'
    }
    context.created_product = create_product(product_data)
