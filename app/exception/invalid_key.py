from http import HTTPStatus

class InvalidKey(Exception):
    def __init__(self, list):
        self.message = {
            "Error": f"Parametro invalido encontrado no corpo da Requisição. As chaves '{str(list)}' são inválidas. Tente novamente."
            }, HTTPStatus.NOT_FOUND