from flask_restful import Resource
from sqlalchemy import func

from src import db
from src.database.models import Film


class AggregationApi(Resource):
    def get(self):
        film = db.session.query(func.count(Film.id)).scalar()
        max_rating = db.session.query(func.max(Film.rating)).scalar()
        min_rating = db.session.query(func.min(Film.rating)).scalar()
        avg_rating = db.session.query(func.avg(Film.rating)).scalar()
        sum_rating = db.session.query(func.sum(Film.rating)).scalar()
        min_length = db.session.query(func.min(Film.length)).scalar()
        max_length = db.session.query(func.min(Film.length)).scalar()
        disney_film = db.session.query(Film).filter_by(
            distributed_by='Disney'
        ).all()
        return {
            'count': film,
            'max': max_rating,
            'min': min_rating,
            'avg': avg_rating,
            'sum': sum_rating,
            'min_length': min_length,
            'max_length': max_length,
            'disney_film': disney_film,

        }
