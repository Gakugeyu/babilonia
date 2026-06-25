from pydantic import BaseModel


class Livro(BaseModel):
    id_: int
    titulo: str
    autor: str
    ano_publicacao: int
    isbn: int

class LivroCriarAtualizar(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int
    isbn: int