from app import app  
from models import Product 
import json


def test_read_product():
    with app.test_client() as client:
        response = client.get('/products/1')  
        assert response.status_code == 200
        product_data = json.loads(response.data)
        assert product_data['name'] == 'Sample Product'


def test_update_product():
    with app.test_client() as client:
        updated_data = {'name': 'New Name'}
        response = client.put('/products/1', json=updated_data)  
        assert response.status_code == 200
        updated_product = Product.get_by_id(1)
        assert updated_product.name == 'New Name'


def test_delete_product():
    with app.test_client() as client:
        response = client.delete('/products/1')  
        assert response.status_code == 200
        deleted_product = Product.get_by_id(1)
        assert deleted_product is None


def test_list_all_products():
    with app.test_client() as client:
        response = client.get('/products')
        assert response.status_code == 200
        products = json.loads(response.data)
        assert len(products) > 0
