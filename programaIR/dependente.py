# Programa alternativo de cálculo do imposto de renda versão 1

from entrada import Texto

# classe de nível mais baixo que contém e manipula um dependente da agenda
class Dependente :
    # construtor dos objetos da classe )
    # caso os dados do dependente não sejam fornecidos, solicita que usuário informe
    def __init__( self, tipo = "", nome_dep = "", nascimento_dep = "", cpf_dep = "" ) :
        self.tipo = tipo
        self.nome_dep = nome_dep
        self.nascimento_dep = nascimento_dep
        self.cpf_dep = cpf_dep
        if nome_dep == "" :
            self.pede_dados( )
 
    # solicita dados de um dependente
    def pede_dados( self ) :
        self.tipo = Texto( "Tipo: ", self.tipo ).string
        self.nome_dep = Texto( "Nome: ", self.nome_dep ).string
        self.nascimento_dep = Texto( "Nascimento: ", self.nascimento_dep ).string
        self.cpf_dep = Texto ( "CPF: ", self.cpf_dep ).string

    # mostra dados de um dependente
    def mostra_dados( self ) :
        return ( "Tipo: %s \nDependente: %s \nNascimento: %s \nCPF: %s" % ( self.tipo, self.nome_dep, self.nascimento_dep, self.cpf_dep ) )
