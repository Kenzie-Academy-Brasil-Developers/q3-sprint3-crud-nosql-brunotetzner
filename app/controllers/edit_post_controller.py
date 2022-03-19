from ..models import Post
from flask import jsonify, request
from ..exception import InvalidKey
from http import HTTPStatus


def edit_post_controller(id):

    data = request.get_json()
    update_post = Post.edit_post(id, **data)

    if type(update_post).__name__ == 'list':
        raise InvalidKey(update_post)
    
    return jsonify(list(update_post)), HTTPStatus.ACCEPTED
