from .db import db

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    is_recommended = db.Column(db.Boolean, nullable=False)
    overall_rating = db.Column(db.Integer, nullable=False)
    comfort_rating = db.Column(db.Integer, nullable=False)
    quality_rating = db.Column(db.Integer, nullable=False)
    fit_rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "is_recommended": self.is_recommended,
            "overall_rating": self.overall_rating,
            "comfort_rating": self.comfort_rating,
            "quality_rating": self.quality_rating,
            "fit_rating": self.fit_rating,
            "description": self.description,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "created_id": self.created_at
        }
