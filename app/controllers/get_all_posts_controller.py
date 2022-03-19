from ..models import Post
from flask import jsonify
from http import HTTPStatus

def get_all_posts_controller():
    posts_list = list(Post.get_all())
    return jsonify(posts_list), HTTPStatus.OK