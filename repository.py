from db import conexao

class NoticiaRespository:

    def add(self, noticia):
        return conexao.insert(noticia)