from models import Product  
from factories import create_fake_product  

def test_read_product_by_id():
   
    new_product = create_fake_product()
    product_id = new_product.save()
    
   
    retrieved_product = Product.get_by_id(product_id)
    
    
    assert retrieved_product.id == product_id
    assert retrieved_product.name == new_product.name


def test_update_product():

    new_product = create_fake_product()
    product_id = new_product.save()
    
    
    updated_name = "Updated Product"
    new_product.name = updated_name
    new_product.save()
    
   
    updated_product = Product.get_by_id(product_id)
    assert updated_product.name == updated_name


def test_delete_product():
    new_product = create_fake_product()
    product_id = new_product.save()
    
    new_product.delete()
    
    deleted_product = Product.get_by_id(product_id)
    assert deleted_product is None


def test_list_all_products():
    
    products_count = 5
    for _ in range(products_count):
        create_fake_product().save()
    
   
    all_products = Product.get_all()
    
    
    assert len(all_products) == products_count


def test_find_product_by_name():
    specific_product = create_fake_product()
    specific_product.save()
    
    
    found_product = Product.find_by_name(specific_product.name)
    
    
    assert found_product.name == specific_product.name

