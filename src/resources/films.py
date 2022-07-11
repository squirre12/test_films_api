import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload

from src import db
from src.database.models import Film
from src.resources.auth import token_required
from src.schemas.films import FilmSchema
from src.services.film_service import FilmService


class FilmListApi(Resource):
    film_schema = FilmSchema()

    def get(self, uuid=None):
        if not uuid:
            films = FilmService.fetch_all_films(db.session).options(
                joinedload(Film.actors)
            ).all()
            return self.film_schema.dump(films, many=True), 200
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        return self.film_schema.dump(film), 200

    def post(self):
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as err:
            return {'Message': str(err)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 201

    def put(self, uuid):
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return "Film not found", 400
        try:
            film = self.film_schema.load(request.json, session=db.session, instance=film)
        except ValidationError as err:
            return {'Message': str(err)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "Film not found", 400
        try:
            film = self.film_schema.load(request.json, session=db.session, instance=film)
        except ValidationError as err:
            return {'Message': str(err)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def delete(self, uuid):
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        db.session.delete(film)
        db.session.commit()
        return '', 204
