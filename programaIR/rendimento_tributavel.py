# Programa alternativo de cálculo do imposto de renda versão 1

from entrada import Texto, Real

# classe de nível mais baixo que contém e manipula os rendimentos tributáveis de pessoa jurídica da declaração
class Rendimento_tributavel :
    # construtor dos objetos da classe
    # caso os dados de rendimentos tributáveis de pessoa jurídica não sejam fornecidos, solicita que usuário informe
    def __init__( self, cnpj_rt = "", nome_fonte_rt = "", rendimento_pj = "", prev = "", imposto = "", sal_13 = "", ir_sal_13 = "" ) :
        self.cnpj_rt = cnpj_rt
        self.nome_fonte_rt = nome_fonte_rt
        self.rendimento_pj = rendimento_pj
        self.prev = prev
        self.imposto = imposto
        self.sal_13 = sal_13
        self.ir_sal_13 = ir_sal_13
        if cnpj_rt == "" :
            self.pede_dados( )
 
    # solicita dados de rendimentos tributáveis de pessoa jurídica
    def pede_dados( self ) :
        self.cnpj_rt = Texto( "CPF/CNPJ da fonte pagadora: ", self.cnpj_rt ).string
        self.nome_fonte_rt = Texto( "Nome da fonte pagadora: ", self.nome_fonte_rt ).string
        self.rendimento_pj = Real ( "Rendimento recebido de PJ: " ).numero
        self.prev = Real ( "Contribuição previdenciária oficial: " ).numero
        self.imposto = Real ( "Imposto retido na fonte: " ).numero
        self.sal_13 = Real ( "13º salário: " ).numero
        self.ir_sal_13 = Real ( "IRRF sobre o 13º salário: " ).numero
  
    # mostra dados de rendimentos tributáveis de pessoa jurídica
    def mostra_dados( self ) :
        return ( "CPF/CNPJ da fonte pagadora: %s \nNome da fonte pagadora: %s \nRendimento recebido de PJ: %s \nContribuição previdenciária de PJ: %s \nImposto retido na fonte: %s \n13º salário: %s \nIRRF sobre 13º salário: %s" % ( self.cnpj_rt, self.nome_fonte_rt, self.rendimento_pj, self.prev, self.imposto, self.sal_13, self.ir_sal_13 ) )
