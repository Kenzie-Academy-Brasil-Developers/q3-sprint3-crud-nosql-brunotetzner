from ..models import Post
from flask import jsonify
from ..exception import PostNotFoundToRemove
from http import HTTPStatus


def delete_post_controller(id):
    remove_post = Post.delete_post(id)

    if len(remove_post) == 0:
        raise PostNotFoundToRemove

    return jsonify(remove_post), HTTPStatus.OK
