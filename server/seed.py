from server import app
from server.models import db, Customer, Item, Review

with app.app_context():
    # Add sample customers
    customer1 = Customer(name='Tal Yuri')
    customer2 = Customer(name='Dana Scully')

    # Add sample items
    item1 = Item(name='Laptop Backpack', price=49.99)
    item2 = Item(name='Insulated Coffee Mug', price=9.99)

    # Add sample reviews
    review1 = Review(comment='Great backpack!', customer=customer1, item=item1)
    review2 = Review(comment='Keeps my coffee hot!', customer=customer1, item=item2)
    review3 = Review(comment='Stylish and spacious.', customer=customer2, item=item1)

    db.session.add_all([customer1, customer2, item1, item2, review1, review2, review3])
    db.session.commit()
