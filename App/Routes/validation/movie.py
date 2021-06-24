from flask_json_schema import JsonSchema, JsonValidationError
from flask import Flask, jsonify, request
from App.__init__ import app

schema = JsonSchema(app)

movie_schema = {
    'required': ['title','year','genre'],
    'properties': {
        'title': { 'type': 'string' },
        'year': { 'type': 'integer' },
        'genre':{'type':'string'}
    }
}