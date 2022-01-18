from flask_restx import Api, Resource
from flask import Flask
from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': 'War and peace'},
    {'id': 1, 'title': 'Clean code'},
    {'id': 2, 'title': 'Clean Arquitecture'},
]


@api.route('/books')
class Booklist(Resource):
    """
    Aqui deverão ser criados metodos com o mesmo nome de HTTP:
    get,post,put,delete
    """

    def get(self,):
        # Aqui iria fazer request para bd para pegar os dados
        return books_db

    def post(self,):
        response = api.payload
        books_db.append(response)
        # no retorno o primeiro sempre é o conteudo e o segundo é o status code
        return books_db, 200
