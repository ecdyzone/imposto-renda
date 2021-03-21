# Programa alternativo de cálculo do imposto de renda versão 1

from entrada import Texto, Real

# classe de nível mais baixo que contém e manipula os redimento sujeito a tributação exclusiva da declaração
class Rendimento_exclusiva_definitiva :
    # construtor dos objetos da classe
    # caso os dados de redimento sujeito a tributação exclusiva não sejam fornecidos, solicita que usuário informe
    def __init__( self, tipo_red = "", cnpj_red = "", nome_fonte_red = "", rendimento_pj = "" ) :
        self.tipo_red = tipo_red
        self.cnpj_red = cnpj_red
        self.nome_fonte_red = nome_fonte_red
        self.rendimento_pj = rendimento_pj
        if cnpj_red == "" :
            self.pede_dados( )
 
    # solicita dados de redimento sujeito a tributação exclusiva
    def pede_dados( self ) :
        self.tipo_red = Texto( "Tipo: ", self.tipo_red ).string
        self.cnpj_red = Texto( "CPF/CNPJ da fonte pagadora: ", self.cnpj_red ).string
        self.nome_fonte_red = Texto( "Nome da fonte pagadora: ", self.nome_fonte_red ).string
        self.rendimento_pj = Real( "Valor do rendimento: "  ).numero
      
    # mostra dados de redimento sujeito a tributação exclusiva
    def mostra_dados( self ) :
        return ( "Tipo: %s \nCPF/CNPJ da fonte pagadora: %s \nNome da fonte pagadora: %s \nValor do rendimento: %s" % ( self.tipo_red, self.cnpj_red, self.nome_fonte_red, self.rendimento_pj ) )
