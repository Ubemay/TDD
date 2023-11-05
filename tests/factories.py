from faker import Faker
from models import Product  

fake = Faker()

def create_fake_product():
    return Product(
        name=fake.name(),
        description=fake.text(),
        price=fake.random_number(digits=2),
        category=fake.random_element(elements=("Electronics", "Clothing", "Books", "Toys")),
        availability=fake.random_element(elements=("In stock", "Out of stock", "Limited")),
    )


def create_electronics_product():
    return Product(
        name=fake.word(),
        description=fake.text(),
        price=fake.random_number(digits=2),
        category="Electronics",
        availability="In stock",
    )

def create_out_of_stock_product():
    return Product(
        name=fake.word(),
        description=fake.text(),
        price=fake.random_number(digits=2),
        category="Books",
        availability="Out of stock",
    )
