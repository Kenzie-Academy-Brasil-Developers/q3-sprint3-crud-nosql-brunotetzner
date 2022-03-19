from ..models import Post
from flask import jsonify
from ..exception import InvalidId
from http import HTTPStatus


def get_specific_post_controller(id): 
  post = list(Post.get_specific(id))

  if not post:
      raise InvalidId
  
  return jsonify(post), HTTPStatus.OK