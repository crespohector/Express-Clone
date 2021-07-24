from .db import db

order_products = db.Table("order_products",
                    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
                    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
                    db.Column('quantity', db.Integer, nullable=False)
                    )
