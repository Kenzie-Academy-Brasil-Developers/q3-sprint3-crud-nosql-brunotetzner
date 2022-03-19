from http import HTTPStatus

class InvalidId(Exception):
    def __init__(self):
        self.message = {
            "Error": "O id informado não existe"
            }, HTTPStatus.NOT_FOUND
