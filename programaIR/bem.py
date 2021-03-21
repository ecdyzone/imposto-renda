# Programa alternativo de cálculo do imposto de renda versão 1

from entrada import Texto, Real

# classe de nível mais baixo que contém e manipula um bem da declaraçao
class Bem :
    # construtor dos objetos da classe (serão vários, um para cada bem)
    # caso os dados do bem não sejam fornecidos, solicita que usuário informe
    def __init__( self, tipo_bem = "", descrição = "", situaçao_2018 = "", situaçao_2019 = "" ) :
        self.tipo_bem = tipo_bem
        self.descrição = descrição
        self.situaçao_2018 = situaçao_2018
        self.situaçao_2019 = situaçao_2019
        if tipo_bem == "" :
            self.pede_dados( )
 
    # solicita dados de um bem
    def pede_dados( self ) :
        self.tipo_bem = Texto( "Tipo de Bem: ", self.tipo_bem ).string
        self.descrição = Texto( "Descrição do Bem: ", self.descrição ).string
        self.situaçao_2018 = Real( "Situação em 2018: " ).numero
        self.situaçao_2019 = Real( "Situação em 2019: " ).numero

    # mostra dados de um bem
    def mostra_dados( self ) :
        return ( "Tipo de Bem: %s \nDescrição: %s \nSituaçao em 31/12/2018 (R$): %s \nSituaçao em 31/12/2019 (R$): %s" % ( self.tipo_bem, self.descrição, self.situaçao_2018, self.situaçao_2019 ) )
