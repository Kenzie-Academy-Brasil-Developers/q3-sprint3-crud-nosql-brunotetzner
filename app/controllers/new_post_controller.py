from ..models import Post
from flask import jsonify, request
from http import HTTPStatus


def new_post_controller():
    data = request.get_json()
    post_add_db = Post(**data)

    return jsonify(post_add_db.create_new_post()), HTTPStatus.CREATED