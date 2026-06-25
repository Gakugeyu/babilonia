import sqlite3
from contextlib import contextmanager


class BancoLocal():
    def __init__(self, nome_banco='banco_local.db'):
        self.nome_banco = nome_banco


    @contextmanager
    def conectar(self):
        conecao = sqlite3.connect(self.nome_banco)
        try:
            yield conecao
            conecao.commit()
        except Exception as e:
            conecao.rollback()
            raise e
        finally:
            conecao.close()

    def inicializar_banco(self):
        with self.conectar() as conecao:
            cursor = conecao.execute('''
                CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    ano_publicacao INTEGER NOT NULL,
                    isbn INTEGER NOT NULL                                    
                )
            ''')

            print("Banco inicializado com sucesso!")
