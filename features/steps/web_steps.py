from behave import when, then
from service.routes import update_product, delete_product, list_all_products, find_product_by_name

@when('the user updates the product details')
def user_updates_product_details(context):
    product_id = context.created_product['id']  
    updated_data = {
        'name': 'Updated Product',
        'description': 'New description',
        'price': 25.0,
        'category': 'Updated Category',
        'availability': 'Out of stock'
    }
    context.updated_product = update_product(product_id, updated_data)

@when('the user deletes the product')
def user_deletes_product(context):
    product_id = context.created_product['id']  
    context.is_deleted = delete_product(product_id)

@when('the user requests to list all products')
def user_requests_list_all(context):
    context.listed_products = list_all_products()

@when('the user searches for the product by name')
def user_searches_by_name(context):
    product_name = context.created_product['name']  
    context.found_product = find_product_by_name(product_name)

