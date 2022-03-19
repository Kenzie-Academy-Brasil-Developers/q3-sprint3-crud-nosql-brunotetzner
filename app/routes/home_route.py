from flask import Flask
from ..controllers import *
from ..exception import *
from http import HTTPStatus

def home_route(app:Flask):
    
    @app.get("/posts")
    def get_all_request():
        return  get_all_posts_controller()


    @app.get("/posts/<int:id>")
    def get_specifc_post_request(id):
        try:
            return get_specific_post_controller(id)
            
        except InvalidId as err:
            return err.message


    @app.post("/posts")
    def create_new_post_request():
        try:
            return  new_post_controller()
            
        except TypeError:
            return {
            "Error": "Há um erro no corpo da requisição. Verifique se há alguma chave faltando"
            }, HTTPStatus.BAD_REQUEST
        
    
    @app.delete("/posts/<int:id>")
    def delete_post_request(id):
        try:
            return delete_post_controller(id)

        except PostNotFoundToRemove as err :
            return err.message


    @app.patch("/posts/<int:id>")
    def edit_post_request(id):
        try:
            return edit_post_controller(id)

        except InvalidKey as err:
            return err.message

        except AttributeError:
            return {
               "Error": "O id informado não existe na base de dados. Tente novamente."
            }, HTTPStatus.NOT_FOUND
        
            