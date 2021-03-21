# Programa alternativo de cálculo do imposto de renda versão 1

from contribuinte import Contribuinte
from dependente import Dependente
from rendimento_tributavel import Rendimento_tributavel
from rendimento_exclusiva_definitiva import Rendimento_exclusiva_definitiva
from bem import Bem
from base_dados import Base_Dados
from declaracao import Declaracao
from entrada import Inteiro, Texto


# classe intermediária que contém e manipula a declaração como um todo
class Menu :
    # construtor do objeto da classe Menu
    def __init__( self, nome_default ) :
        self.declaracao = Declaracao( nome_default )
        
    # solicita dados e cria os campos necessários na declaração
    def cria( self ) :
        while True :            # interage repetidamente até encerrar
            # apresenta o menu na tela
            print( '''
   1 - Inserir dados do contribuinte
   2 - Inserir dependente
   3 - Inserir rendimento tributável de pessoa jurídica
   4 - Inserir rendimento sujeito à tributação exclusiva/definitiva
   5 - Inserir bem

   0 - Voltar ao menu principal
            ''' )
            opcao = Inteiro( "Escolha opção: ", 0, 5 ).valor
            
            # trata a opção escolhida pelo usuário
            if opcao == 0 :
                break
            elif opcao == 1 :
                self.declaracao.cria_contribuinte( Contribuinte( cpf = self.declaracao.declaracao[6] ) ) # passa o cpf introduzido no início do programa ao cpf do objeto criado na classe contribuinte
            elif opcao == 2 :
                self.declaracao.cria_dependente( Dependente( ) )
            elif opcao == 3 :
                self.declaracao.cria_rendimento_tributavel( Rendimento_tributavel( ) )
            elif opcao == 4 :
                self.declaracao.cria_rendimento_exclusiva_definitiva( Rendimento_exclusiva_definitiva( ) )
            elif opcao == 5 :
                self.declaracao.cria_bem( Bem( ) )

    def altera( self ) :
        while True :            # interage repetidamente até encerrar
            # apresenta o menu na tela
            print( '''
   1 - Alterar dados do contribuinte
   2 - Alterar dependente
   3 - Alterar rendimento tributável de pessoa jurídica
   4 - Alterar rendimento sujeito à tributação exclusiva/definitiva
   5 - Alterar bem

   0 - Voltar ao menu principal
            ''' )
            opcao = Inteiro( "Escolha opção: ", 0, 5 ).valor
            
            # trata a opção escolhida pelo usuário
            if opcao == 0 :
                break
            elif opcao == 1 :
                self.declaracao.altera_contribuinte( Texto( "\nNome do contribuinte: " ).string )
            elif opcao == 2 :
                self.declaracao.altera_dependente( Texto( "\nNome do dependente: " ).string )
            elif opcao == 3 :
                self.declaracao.altera_rendimento_tributavel( Texto( "\nCPF/CNPJ da fonte pagadora: " ).string )
            elif opcao == 4 :
                self.declaracao.altera_rendimento_exclusiva_definitiva( Texto( "\nCPF/CNPJ da fonte pagadora: " ).string )
            elif opcao == 5 :
                self.declaracao.altera_bem( Texto( "\nDescrição do bem: " ).string )

    def apaga( self ) :
        while True :            # interage repetidamente até encerrar
            # apresenta o menu na tela
            print( '''
   1 - Apagar dados do contribuinte
   2 - Apagar dependente
   3 - Apagar rendimento tributável de pessoa jurídica
   4 - Apagar rendimento sujeito à tributação exclusiva/definitiva
   5 - Apagar bem

   0 - Voltar ao menu principal
            ''' )
            opcao = Inteiro( "Escolha opção: ", 0, 5 ).valor
            
            # trata a opção escolhida pelo usuário
            if opcao == 0 :
                break
            elif opcao == 1 :
                self.declaracao.apaga_contribuinte( Texto( "\nContribuinte: " ).string )
            elif opcao == 2 :
                self.declaracao.apaga_dependente( Texto( "\nDependente: " ).string )
            elif opcao == 3 :
                self.declaracao.apaga_rendimento_tributavel( Texto( "\nRendimento tributável: " ).string )
            elif opcao == 4 :
                self.declaracao.apaga_rendimento_exclusiva_definitiva( Texto( "\nRendimento exclusiva/definitiva: " ).string )
            elif opcao == 5 :
                self.declaracao.apaga_bem( Texto( "\nBem: " ).string )

