import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorsSchema


class ActorListApi(Resource):
    actor_schema = ActorsSchema()

    def get(self, uuid=None):
        if not uuid:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return "", 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as err:
            return {"message": str(err)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return 400
        try:
            actor = self.actor_schema.load(request.json, session=db.session, instance=actor)
        except ValidationError as err:
            return {"message": str(err)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201


    def patch(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first
        if not actor:
            return 400
        try:
            actor = self.actor_schema.load(request.json, session=db.session, instance=actor)
        except ValidationError as err:
            return {"message": str(err)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201


    def delete(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return {'message': 'actor not found'}
        db.session.delete(actor)
        db.session.commit()
        return '', 204

