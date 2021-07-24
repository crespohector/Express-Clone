from .db import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    small_quantity = db.Column(db.Integer, nullable = False)
    medium_quantity = db.Column(db.Integer, nullable = False)
    large_quantity = db.Column(db.Integer, nullable = False)
    category = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.String(255), nullable = False)

    reviews = db.relationship('Review', backref="product", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "small_quantity": self.small_quantity,
            "mediumn_quantity": self.medium_quantity,
            "large_quantity": self.large_quantity,
            "category": self.category,
            "description": self.description,
            "image_url": self.image_url
        }
