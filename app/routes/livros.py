from fastapi import APIRouter,Depends
from typing import Annotated
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


from app.banco_de_dados.livro_repositorio import LivroRepositorio
from app.modelos.livros import Livro, LivroCriarAtualizar
from app.dependencias import obter_livro_repositorio

templates = Jinja2Templates(directory="templates")


router = APIRouter(prefix="/api/livros")
front_router = APIRouter(prefix="/livros")

@router.get("/")
def listar_livros():
   pass
    
##############################################BACK-END##############################################
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

##############################################FRONT-END##############################################
@front_router.get("/",response_class=HTMLResponse)
def front_listar_livros(request: Request, livro_repositorio: Annotated[LivroRepositorio, Depends(obter_livro_repositorio)]):
    livros = livro_repositorio.listar_livros()
    return templates.TemplateResponse(request=request, name="index.html", context={"livros": livros})


@front_router.get("/novo", response_class=HTMLResponse)
async def front_cadastrar_livro(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

