from app.models import db, Review
from faker import Faker

fake = Faker()

# Adds a review, you can add other reviews here if you want
def seed_reviews():

    review = Review(title="Great outfit!",
                is_recommended=True,
                overall_rating=5,
                comfort_rating=5,
                quality_rating=5,
                fit_rating=5,
                description="It feels super soft and nice! Love it!",
                user_id=1,
                product_id=1,
                )

    db.session.add(review)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the reviews table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
