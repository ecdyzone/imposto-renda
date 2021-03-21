# Programa alternativo de cálculo do imposto de renda versão 1

from entrada import Texto

# classe de nível mais baixo que contém e manipula um contribuinte da declaração
class Contribuinte :
    # construtor dos objetos da classe (serão vários, um para cada contribuinte)
    # caso os dados do contribuinte não sejam fornecidos, solicita que usuário informe
    def __init__( self, nome = "", nascimento = "", endereço = "", cpf = "", telefone = "", ocupaçao = "" ) :
        self.nome = nome
        self.nascimento = nascimento
        self.endereço = endereço
        self.cpf = cpf
        self.telefone = telefone
        self.ocupaçao = ocupaçao
        if nome == "" :
            self.pede_dados( )
 
    # solicita dados de um contribuinte
    def pede_dados( self ) :
        self.nome = Texto( "Nome: ", self.nome ).string
        self.nascimento = Texto( "Nascimento: ", self.nascimento ).string
        self.endereço = Texto ( "Endereço: ", self.endereço ).string
        #self.cpf = Texto ( "CPF: ", self.cpf ).string  # linha utilizada antes de trazer o cpf nos argumentos via base de dados. Olhar linha 44 do menu. Ao desativá-la, torna-se o cpf inalterável, já que a declaracao esta vinculada a ele com identificador.
        self.telefone = Texto ( "Telefone: ", self.telefone ).string
        self.ocupaçao = Texto ( "Ocupação Principal: ", self.ocupaçao ).string
  
    # mostra dados de um contribuinte
    def mostra_dados( self ) :
        return ( "Nome: %s \nNascimento: %s \nEndereço: %s \nCPF: %s \nTelefone: %s \nOcupação Principal: %s" % ( self.nome, self.nascimento, self.endereço, self.cpf, self.telefone, self.ocupaçao ) )
