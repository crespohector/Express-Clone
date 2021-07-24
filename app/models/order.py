from .db import db
from .order_products import order_products

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable = False)
    date_order_placed = db.Column(db.DateTime, nullable = False)

    products = db.relationship('Product', secondary=order_products, lazy="subquery", backref=db.backref('orders', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_amount": self.total_amount,
            "date_order_placed": self.date_order_placed
        }
