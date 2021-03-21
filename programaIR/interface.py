# Programa alternativo de cálculo do imposto de renda versão 1

from menu import Menu
from entrada import Inteiro

class Interface :
    # construtor do objeto da classe Interface
    # cria um objeto da classe declaração, carregando os dados do disco, se existirem
    # opera o menu do usuário
    def __init__( self, nome_default ) :
        self.menu = Menu( nome_default )    # cria nova declaração
        self.opçoes( )            # realiza a interação com o usuário
        
    # mostra menu principal
    def opçoes( self ) :
        while True :            # interage repetidamente até encerrar
            # apresenta o menu na tela
            print( '''
   1 - Inserir novos dados na declaração
   2 - Alterar dados já inseridos 
   3 - Apagar dados já inseridos
   4 - Gravar declaração
   5 - Resumo da declaração
   6 - Calcular imposto devido
   7 - Emitir declaração

   0 - Sair do programa
            ''' )   
            # solicita e valida entrada do usuário
            opcao = Inteiro( "Escolha opção: ", 0, 7 ).valor
            
            # trata a opção escolhida pelo usuário
            if opcao == 0 :
                if not self.menu.declaracao.modificada :
                    break
                if input( "Sai sem gravar declaração existente (S/N)? " ).lower( ) == "s" :
                    break
            elif opcao == 1 :
                self.menu.cria( )
            elif opcao == 2 :
                self.menu.altera( )
            elif opcao == 3 :
                self.menu.apaga( )
            elif opcao == 4 :
                self.menu.declaracao.grava( )
            elif opcao == 5 :
                self.menu.declaracao.resumo( )
            elif opcao == 6 :
                self.menu.declaracao.calculadora( )
            elif opcao == 7 :
                self.menu.declaracao.declara( )
