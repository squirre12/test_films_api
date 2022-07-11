"""
SELECT QUERIES
"""
from sqlalchemy import and_
from sqlalchemy.testing import in_

from src import db
from src.database import models

films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
harry_potter2 = db.session.query(models.Film).filter(
    models.Film.title == 'Harry Potter and Chamber of Secrets'
).first()
# print(harry_potter2)
harry_potter3 = db.session.query(models.Film).filter_by(
    title='Harry Potter and the Prizoner of Azkaban'
).first()
# print(harry_potter3)
add_satatement_harry_potter = db.session.query(models.Film).filter(
    models.Film.title != 'Harry Potter and Chamber of Secret',
    models.Film.rating >= 7.5
).all()
# print(add_satatement_harry_potter)

add_satatement_harry_potter_and = db.session.query(models.Film).filter(
    and_(
        models.Film.title != 'Harry Potter and Chamber of Secret',
        models.Film.rating >= 7.5
    )
).all()

deathly_halows = db.session.query(models.Film).filter(
    models.Film.title.like('%Deathly Hallows%')
).all()
# print(deathly_halows)
harry_potter_sorted_by_length = db.session.query(models.Film).filter(
    ~models.Film.length.in_([146, 161]))[:2]
# print(harry_potter_sorted_by_length)
"""
QUERING WITH JOINS 
"""

films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
# print(films_with_actors)

