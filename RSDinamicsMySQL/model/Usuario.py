from model.Pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, email, senha, profissao, genero, nascimento, id_usuario=None):
        super(Usuario, self).__init__(nome, genero)
        self.id_usuario = id_usuario
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.profissao = profissao

    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()
