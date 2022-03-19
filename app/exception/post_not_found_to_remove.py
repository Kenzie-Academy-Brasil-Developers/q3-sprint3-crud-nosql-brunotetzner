from http import HTTPStatus
class PostNotFoundToRemove(Exception):
    def __init__(self):
     self.message = {
         "Error": "Post não encontrado. Isso provavelmente quer dizer que esse post não existe. Tente novamente"
         }, HTTPStatus.NOT_FOUND