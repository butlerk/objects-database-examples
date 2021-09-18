from fruits_db import session, Fruit, Vegetable

vegetables = session.query(Vegetable).all()
for vegetable in vegetables:
    print()
    print(f'Vegetable: { vegetable.name }')
    print(f'Price: { vegetable.price_cents } cents')
    print(f'Colour: { vegetable.colour }')

fruits = session.query(Fruit).all()
for fruit in fruits:
    print()
    print(f'Fruit: {fruit.name}')
    print(f'Price: {fruit.price_cents} cents')
    double = fruit.price_cents * 2
    print(f'Double price: {double}')
