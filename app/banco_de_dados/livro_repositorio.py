from app.banco_de_dados.local import BancoLocal
from app.modelos.livros import Livro, LivroCriarAtualizar


class LivroRepositorio:
    def __init__(self):
        self.banco = BancoLocal()
        self.banco.inicializar_banco()


    def listar_livros(self) -> list[Livro]:
        with self.banco.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id_, titulo, autor, ano_publicacao, isbn FROM livros")
            linhas = cursor.fetchall()
            livros = [Livro(id_=linha[0], titulo=linha[1], autor=linha[2], ano_publicacao=linha[3], isbn=linha[4]) 
                      for linha in linhas]
            return livros

    def cadastrar_livro(self, livro: LivroCriarAtualizar) -> Livro:
        with self.banco.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, isbn) VALUES (?,?,?,?)",
            (livro.titulo, livro.autor, livro.ano_publicacao, livro.isbn))
            livro_id = cursor.lastrowid
            return Livro(id_=livro_id, titulo=livro.titulo, autor=livro.autor, ano_publicacao=livro.ano_publicacao, isbn=livro.isbn)