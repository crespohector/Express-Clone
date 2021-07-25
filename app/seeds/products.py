from app.models import db, Product

# categories: Tops. Dresses, Jeans, Shorts, Dress Pants

# Adds a product, you can add other products here if you want
def seed_products():

    top1 = Product(title="The Good Vibe",
                    price=20.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="tops",
                    description="This tee is anything but basic thanks to supersoft stretch fabric, a fitted, double-layered design and a lightweight feel.",
                    image_url="https://i.pinimg.com/originals/a8/6c/8b/a86c8bfe4c4bbcd902543063c9af0d63.jpg"
                    )

    top2 = Product(title="Cotton t-shirt",
                    price=10.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="tops",
                    description="A staple piece for cooler months, this cotton tee promises a polished look and comfortable fit.",
                    image_url="https://cdn.shopify.com/s/files/1/0806/7971/products/Worn-Free-Custom-Shop-Womens-Tee-Teal_2000x.jpg?v=1598677116"
                    )

    top3 = Product(title="Shirt sweat t-shirt",
                    price=10.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="tops",
                    description="A staple piece for cooler months, this cotton tee promises a polished look and comfortable fit.",
                    image_url="test"
                    )

    top4 = Product(title="White collared shirt",
                    price=25.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="tops",
                    description="A well fitted, comfortable, and a lightweight feel.",
                    image_url="https://i.pinimg.com/originals/c6/fd/93/c6fd93526f4f19c5ebe8ee700408e484.jpg"
                    )

    top5 = Product(title="White top",
                    price=20.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="tops",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS1Bnqh4u19GNUNqV_74-PEy5MeUOAROYktw&usqp=CAU"
                    )


    dress1 = Product(title="White summer dress",
                    price=40.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="dresses",
                    description="This eye-catching design a match for any party, dinner date or day out this season.",
                    image_url="https://ae01.alicdn.com/kf/HTB1MLuUdROD3KVjSZFFq6An9pXaC/Clothes-Dress-Summer-Women-S-Sundress-Korean-Style-Dresses-Woman-Free-Shiping-White-Summer-Dress-Sexy.jpg_Q90.jpg_.webp"
                    )

    dress2 = Product(title="Light pink dress with flower design",
                    price=45.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="dresses",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="https://i.pinimg.com/originals/f0/ba/e2/f0bae23de7a4f9d5791ddbeaa937e8d0.jpg"
                    )

    dress3 = Product(title="Yellow Dress",
                    price=35.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="dresses",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="https://images.unsplash.com/photo-1612722432474-b971cdcea546?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8d29tYW4lMjBkcmVzc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"
                    )

    dress4 = Product(title="Simple dress",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="dresses",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxYLN1oUlaf2mHP7AydrH5jQ1JSanweCXKsg&usqp=CAU"
                    )


    jean1 = Product(title="Women's jeans",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="jeans",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="test jeans"
                    )

    jean2 = Product(title="jeans 2",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="jeans",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="test 3 jeans"
                    )

    jean3 = Product(title="jeans 3",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="jeans",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaZIdLqaL68bJOEDxAWgnOI7ryAZt9Ri2Osw&usqp=CAU"
                    )


    shorts1 = Product(title="shorts 1",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="shorts",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong..",
                    image_url="=="
                    )

    shorts2 = Product(title="shorts 2",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="shorts",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong.",
                    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNtaGqAXhAYcgghjVWjXrc4IrVYSJejhz2lg&usqp=CAU"
                    )

    shorts3 = Product(title="shorts 3",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="shorts",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong.",
                    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR14g2USpBPIbnZnbehV1tNEl6Td51IEDPGsw&usqp=CAU"
                    )

    dress_pants1 = Product(title="dress pants 1",
                    price=30.00,
                    small_quantity=10,
                    medium_quantity=10,
                    large_quantity=10,
                    category="dress pants",
                    description="This fitted, supersoft tee pulls together any look. Style it solo or layer it up - you can't go wrong.",
                    image_url="test"
                    )

    db.session.add(top1)
    db.session.add(top2)
    db.session.add(top3)
    db.session.add(top4)
    db.session.add(top5)
    db.session.add(dress1)
    db.session.add(dress2)
    db.session.add(dress3)
    db.session.add(dress4)
    db.session.add(jean1)
    db.session.add(jean2)
    db.session.add(jean3)
    db.session.add(shorts1)
    db.session.add(shorts2)
    db.session.add(shorts3)
    db.session.add(dress_pants1)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the products table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
