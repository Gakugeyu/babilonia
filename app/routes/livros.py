from fastapi import APIRouter,Depends
from typing import Annotated

from app.banco_de_dados.livro_repositorio import LivroRepositorio
from app.modelos.livros import Livro, LivroCriarAtualizar
from app.dependencias import obter_livro_repositorio
router = APIRouter(prefix="/api/livros")


@router.get("/")
def listar_livros():
   pass
    

@router.post("/", response_model= Livro | None)
def cadastrar_livro(livrorepositorio: Annotated[LivroRepositorio, Depends(obter_livro_repositorio)], livro: LivroCriarAtualizar):
    return livrorepositorio.cadastrar_livro(livro)


@router.get("/")
def procurar_livro():
    pass

@router.put("/")
def atualizar_livro():
    pass

@router.delete("/")
def deletar_livro():
    pass