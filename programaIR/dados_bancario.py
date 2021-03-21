# Programa alternativo de cálculo do imposto de renda versão 1

from entrada import Real

# classe de nível mais baixo que contém e manipula os dados bancários da declaração
class Dados_bancario :
    # construtor dos objetos da classe
    # caso os dados bancários não sejam fornecidos, solicita que usuário informe
    def __init__( self, banco = "", agencia = "", conta = "", dv = "" ) :
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.dv = dv
        if banco == "" :
            self.pede_dados( )
 
    # solicita dados de um contato
    def pede_dados( self ) :
        self.banco = Real( "Banco: " , 'inteiro').numero
        self.agencia = Real( "Agência: ", 'inteiro' ).numero
        self.conta = Real ( "Conta corrente:  ", 'inteiro' ).numero
        self.dv = Real ( "Dígito verificador: ", 'inteiro' ).numero       

    # mostra dados de um contato
    def mostra_dados( self ) :
        return ( "Banco: %s \nAgência: %s \nConta Corrente: %s \nDV: %s" % ( self.banco, self.agencia, self.conta, self.dv ) )
