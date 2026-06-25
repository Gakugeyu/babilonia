from fastapi import Depends
from typing import Annotated

from app.banco_de_dados.local import BancoLocal
from app.banco_de_dados.livro_repositorio import LivroRepositorio

banco_de_dados = BancoLocal()

def obter_banco_de_dados_local() -> BancoLocal:
    return banco_de_dados

def obter_livro_repositorio(banco_local: Annotated[BancoLocal, Depends(obter_banco_de_dados_local)]) -> LivroRepositorio:
    return LivroRepositorio()