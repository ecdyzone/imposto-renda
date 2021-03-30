# Programa alternativo de cálculo do imposto de renda versão 1

from contribuinte import Contribuinte
from dependente import Dependente
from rendimento_tributavel import Rendimento_tributavel
from rendimento_exclusiva_definitiva import Rendimento_exclusiva_definitiva
from bem import Bem
from dados_bancario import Dados_bancario
from base_dados import Base_Dados

# classe intermediária que contém e manipula a declaração como um todo


class Declaracao :
    # construtor do objeto da classe Declarao
    # carrega a declaração da base de dados, se existir, senão inicializa uma nova
    def __init__( self, nome_default ) :
        self.modificada = False  # nada para salvar no disco
        self.base_dados = Base_Dados( nome_default )  # base de dados que contém a declaração
        self.declaracao = self.base_dados.recupera( )  # lê a base de dados no disco
        self.imposto = -1   # inicia em -1 | após cálculo de imposto, self.imposto >= 0 (ver método .declara())
        self.restituicao = False    # False = imposto a pagar / True = imposto a restituir 
        self.desconto_completo_escolhido = False  # False = calculo simplificado / True = calculo completo
      
        

    # PESQUISA
    def pesquisa_contribuinte( self, nome ) :    
        mnome = nome.lower( )
        for p, e in enumerate( self.declaracao[0] ) :
            if e.nome.lower( ) == mnome :
                return p
        return None

    def pesquisa_dependente( self, nome_dep ) :    
        mnome_dep = nome_dep.lower( )
        for p, e in enumerate( self.declaracao[1] ) :
            if e.nome_dep.lower( ) == mnome_dep :
                return p
        return None

    def pesquisa_rendimento_tributavel( self, cnpj_rt ) :    
        mcnpj_rt = cnpj_rt.lower( )
        for p, e in enumerate( self.declaracao[2] ) :
            if e.cnpj_rt.lower( ) == mcnpj_rt :
                return p
        return None

    def pesquisa_rendimento_exclusiva_definitiva( self, cnpj_red ) :    
        mcnpj_red = cnpj_red.lower( )
        for p, e in enumerate( self.declaracao[3] ) :
            if e.cnpj_red.lower( ) == mcnpj_red :
                return p
        return None

    def pesquisa_bem( self, descrição ) :    
        mdescrição = descrição.lower( )
        for p, e in enumerate( self.declaracao[4] ) :
            if e.descrição.lower( ) == mdescrição :
                return p
        return None

    # CRIA
    def cria_contribuinte( self, contribuinte ) :
        #para criar apenas 1 contribuinte
        if self.declaracao[0] == [] :
            self.declaracao[0].append( contribuinte )
            self.modificada = True
            print( "\nContribuinte criado" )
        else :
            print( "\nContribuinte já existente. Só é possível criar um contribuinte por declaração" )

    def cria_dependente( self, dependente ) :      
        self.declaracao[1].append( dependente )
        self.modificada = True
        print( "\nDependente criado" )

    def cria_rendimento_tributavel( self, rendimento_tributavel ) :      
        self.declaracao[2].append( rendimento_tributavel )
        self.modificada = True
        print( "\nRendimento tributável criado" )

    def cria_rendimento_exclusiva_definitiva( self, rendimento_exclusiva_definitiva ) :      
        self.declaracao[3].append( rendimento_exclusiva_definitiva )
        self.modificada = True
        print( "\nRendimento exclusiva/definitiva criado" )

    def cria_bem( self, bem ) :      
        self.declaracao[4].append( bem )
        self.modificada = True
        print( "\nBem criado" )

    def cria_dados_bancario( self, dados_bancarios ) :      
        self.declaracao[5].append( dados_bancarios )
        self.modificada = True
        print( "\nDados Bancários registrados" )

        
        
    # APAGA
    def apaga_contribuinte( self, contribuinte ) :     
        p = self.pesquisa_contribuinte( contribuinte )
        if p != None :
            del self.declaracao[0][ p ]
            self.modificada = True
            print( "\nContribuinte apagado" )
        else :
            print( "\nContribuinte não encontrado" )

    def apaga_dependente( self, dependente ) :     
        p = self.pesquisa_dependente( dependente )
        if p != None :
            del self.declaracao[1][ p ]
            self.modificada = True
            print( "\nDependente apagado" )
        else :
            print( "\nDependente não encontrado" )

    def apaga_rendimento_tributavel( self, rendimento_tributavel ) :     
        p = self.pesquisa_rendimento_tributavel( rendimento_tributavel )
        if p != None :
            del self.declaracao[2][ p ]
            self.modificada = True
            print( "\nRendimento tributável apagado" )
        else :
            print( "\nRendimento tributável não encontrado" )

    def apaga_rendimento_exclusiva_definitiva( self, rendimento_exclusiva_definitiva ) :     
        p = self.pesquisa_rendimento_exclusiva_definitiva( rendimento_exclusiva_definitiva )
        if p != None :
            del self.declaracao[3][ p ]
            self.modificada = True
            print( "\nRendimento exclusiva/definitiva apagado" )
        else :
            print( "\nRendimento exclusiva/definitiva não encontrado" )

    def apaga_bem( self, bem ) :     
        p = self.pesquisa_bem( bem )
        if p != None :
            del self.declaracao[4][ p ]
            self.modificada = True
            print( "\nBem apagado" )
        else :
            print( "\nBem não encontrado" )

    #ALTERA

    def altera_contribuinte( self, contribuinte ) :        
        p = self.pesquisa_contribuinte( contribuinte )
        if p != None :
            print( "\nEncontrado:\n" )
            print('%s' % self.declaracao[0][ p ].mostra_dados( ))
            print( "\nInsira os novos dados\n" )
            self.declaracao[0][ p ].pede_dados( )
            self.modificada = True
            print( "\nContribuinte alterado" )
        else :
            print( "\nContribuinte não encontrado" )

    def altera_dependente( self, dependente ) :        
        p = self.pesquisa_dependente( dependente )
        if p != None :
            print( "\nEncontrado:\n" )
            print('%s' % self.declaracao[1][ p ].mostra_dados( ))
            print( "\nInsira os novos dados\n" )
            self.declaracao[1][ p ].pede_dados( )
            self.modificada = True
            print( "\nDependente alterado" )
        else :
            print( "\nDependente não encontrado" )

    def altera_rendimento_tributavel( self, rendimento_tributavel ) :        
        p = self.pesquisa_rendimento_tributavel( rendimento_tributavel )
        if p != None :
            print( "\nEncontrado:\n" )
            print('%s' % self.declaracao[2][ p ].mostra_dados( ))
            print( "\nInsira os novos dados\n" )
            self.declaracao[2][ p ].pede_dados( )
            self.modificada = True
            print( "\nRendimento tributável alterado" )
        else :
            print( "\nRendimento tributável não encontrado" )

    def altera_rendimento_exclusiva_definitiva( self, rendimento_exclusiva_definitiva ) :        
        p = self.pesquisa_rendimento_exclusiva_definitiva( rendimento_exclusiva_definitiva )
        if p != None :
            print( "\nEncontrado:\n" )
            print('%s' % self.declaracao[3][ p ].mostra_dados( ))
            print( "\nInsira os novos dados\n" )
            self.declaracao[3][ p ].pede_dados( )
            self.modificada = True
            print( "\nRendimento exclusiva/definitiva alterado" )
        else :
            print( "\nRendimento exclusiva/definitiva não encontrado" )

    def altera_bem( self, bem ) :        
        p = self.pesquisa_bem( bem )
        if p != None :
            print( "\nEncontrado:\n" )
            print('%s' % self.declaracao[4][ p ].mostra_dados( ))
            print( "\nInsira os novos dados\n" )
            self.declaracao[4][ p ].pede_dados( )
            self.modificada = True
            print( "\nBem alterado" )
        else :
            print( "\nBem não encontrado" )

    def altera_dados_bancario( self) :        
        print( "\nInsira os novos dados\n" )
        self.declaracao[5][ 0 ].pede_dados( )
        self.modificada = True
        print( "\nDados Bancários alterados" )
        
    # salva declaração no disco
    def grava( self ) :
        self.base_dados.salva( self.declaracao )
        self.modificada = False

    # mostra toda a declaração
    def resumo( self ) :
        print( "-----------\nDeclaração\n\n-----------\nContribuinte\n" )
        i = 0 # contador
        while i < len(self.declaracao) :
            
            for e in self.declaracao[i] :
                print ('%s' % e.mostra_dados( ))
                print ("\n")
            i += 1
            if i == 1 :
                titulo = 'Dependentes'
            elif i == 2 :
                titulo = 'Rendimentos Tributáveis'
            elif i == 3 :
                titulo = 'Rendimentos com Tributação Exclusiva/Definitiva'
            elif i == 4 :
                titulo = 'Bens'
            else :
                break
                
            print( "---\n%s\n" % (titulo) )

        #evita printar imposto = -1
        retorna_imposto = False
        if self.imposto == -1:
            self.imposto = 0
            retorna_imposto = True
        

        if not self.restituicao and not self.desconto_completo_escolhido :
            #simplificado a pagar
            print( "---\nCálculo Simplificado\nImposto a pagar (R$): %.2f" % self.imposto)
        if self.restituicao and not self.desconto_completo_escolhido :
            #simplificado a restituir
            print( "---\nCálculo Simplificado\nImposto a ser restituido (R$): %.2f" % self.imposto)
        if not self.restituicao and self.desconto_completo_escolhido :
            #completo a pagar
            print( "---\nCálculo Completo\nImposto a pagar (R$): %.2f" % self.imposto)
        if self.restituicao and self.desconto_completo_escolhido :
            #completo a restituir
            print( "---\nCálculo Completo\nImposto a ser restituído (R$): %.2f" % self.imposto)
                
        if self.restituicao :
            #mostra dados bancarios em caso de restituicao
            print('\nDados Bancários para restituição:\n\n%s\n' % self.declaracao[5][0].mostra_dados( ))

        if retorna_imposto :
            self.imposto = -1
                      
        print( "-----------\n" )
        
    # calcula imposto devido

    def pergunta_dados_bancarios (self) :
        if self.declaracao[5] == [] :
            print( "\nInsira seus dados bancários:\n" )
            self.cria_dados_bancario( Dados_bancario () )
        else:
            dados = self.declaracao[5][0].mostra_dados()
            if input( "\nDeseja alterar seus dados bancários (S/N) ?\n\n%s\n\n" % dados ).lower( ) != "s":
                print ('Dados bancários inalterados')
            else:
                self.altera_dados_bancario() # linha 196
    
    def calculadora( self ) :
        #Calculo do simplificado (y1)
       contador = 0
       Soma_Salarios = 0
       while contador < len(self.declaracao[2]) : #numero de rendimentos tributaveis
           Soma_Salarios += float(self.declaracao[2][contador].rendimento_pj)
           contador += 1
       
       SalBruto = float(Soma_Salarios)
       DescS = SalBruto * 0.2
       if DescS > 15000:
           DescS = 15000
       b1 = SalBruto - DescS
       ir1 = 0
       if b1 <= 22847.76 :
           ir1 = b1*0
       elif b1<=33919.80 :
           ir1 = b1*0.075 - 1713.58
       elif b1<=45012.61 :
           ir1 = b1*0.15 - 4257.57
       elif b1<= 55979.16 :
           ir1 = b1*0.225 - 7633.51
       else :
           ir1 = b1*0.275 - 10432.32
       try:    
           ip = float(self.declaracao[2][0].imposto)
       except IndexError:
           print( "\nNão há nenhum registro de imposto retido na fonte. Verifique seus registros de rendimento tributável.")
           ip = 0
           return
       y1 = ir1 - ip


       #Calculo do completo (y2)
       DescD = 6000
       D = len(self.declaracao[1])
       try:
           cont_prev = float(self.declaracao[2][0].prev)
       except IndexError:
           print( "\nNão há nenhum registro de contribuição previdenciária. Verifique seus registros de rendimento tributável.")
           cont_prev = 0
           return
           
       b2 = SalBruto - cont_prev - (D*DescD)
       ir2 = 0
       if b2 <= 22847.76 :
           ir2 = b2*0
       elif b2<=33919.80 :
           ir2 = b2*0.075 - 1713.58
       elif b2<=45012.61 :
           ir2 = b2*0.15 - 4257.57
       elif b2<= 55979.16 :
           ir2 = b2*0.225 - 7633.51
       else :
           ir2 = b2*0.275 - 10432.32
       y2 = ir2 - ip


       # EXIBE OS DOIS CALCULOS
       
       print ("\nCálculo Simplificado: %.2f" % y1)
       
       print ("Cálculo Completo: %.2f" % y2)

       #COMPARAÇÕES E ESCOLHA AUTOMÁTICA     
       
       if y1 - y2 > 0 :
           # y2 é a melhor escolha
           self.desconto_completo_escolhido = True
           print( "\nOpção de Cálculo Completo selecionado!")
           if y2 < 0 :
               self.imposto = - y2
               
               print( "\nCálculo Completo\nImposto a ser restituído (R$): %.2f" % self.imposto)
               #PEDIR DADOS BANCÁRIOS
               self.pergunta_dados_bancarios()
               self.restituicao = True
           else :
               self.imposto = y2
               print( "\nCálculo Completo\nImposto a pagar (R$): %.2f" % self.imposto)
       else:
           # y1 é a melhor escolha
           print( "\nOpção de Cálculo Simplificado selecionado!")
           if y1 < 0 :
               self.imposto = - y1
               print( "\nCálculo Simplificado\nImposto a ser restituido (R$): %.2f" % self.imposto)
               #PEDIR DADOS BANCÁRIOS
               self.pergunta_dados_bancarios()
               self.restituicao = True
           else :
               self.imposto = y1
               print( "\nCálculo Simplificado\nImposto a pagar (R$): %.2f" % self.imposto)

           
    # exporta declaração para arquivo de texto
    def declara( self ) :    
        if len( self.declaracao[0] ) == 0 : # verifica se existem dados do contribuinte
            print ("\nERRO: Não há contribuinte. Preencha os dados de contribuinte e tente novamente.")

        elif len( self.declaracao[2] ) == 0: # verifica se existe fonte de rendimento tributável 
            print ("\nERRO: Não há rendimentos tributáveis. Preencha os dados de rendimento tributável e tente novamente.")

        elif self.imposto < 0 : # verifica se calculo do imposto foi feito
            print ("\nERRO: Efetue o cálculo do imposto e tente novamente.")
        
        else :
            if self.modificada :
                if input( "A declaração foi modificada. Deseja emitir a declaração sem salvar as alterações feitas (S/N) ? " ).lower( ) != "s" :
                    return
            print ('')
            self.resumo()
            if input( "\nEstas são as informações a serem declaradas.\nConfirme se estão corretas antes de continuar. (S/N) " ).lower( ) != "s" :
                print ( '\nDeclaração não emitida.')
                return
                
            nome_declaracao = str(self.declaracao[0][0].cpf) + ".txt"
            declarando = open(nome_declaracao, "w")

            declarando.write( "-----------\nDeclaração\n\n-----------\nContribuinte\n\n" )
            i = 0 # contador

            while i < len(self.declaracao) :
                
                for e in self.declaracao[i] :
                    declarando.write ("%s\n\n" % e.mostra_dados( ) )
                i += 1
                if i == 1 :
                    titulo = 'Dependentes'
                elif i == 2 :
                    titulo = 'Rendimentos Tributáveis'
                elif i == 3 :
                    titulo = 'Rendimentos com Tributação Exclusiva/Definitiva'
                elif i == 4 :
                    titulo = 'Bens'
                else :
                    break
                    
                declarando.write( "---\n%s\n\n" % (titulo) )

            if not self.restituicao and not self.desconto_completo_escolhido :
                #write simplificado a pagar
                declarando.write( "---\nCálculo Simplificado\nImposto a pagar (R$): %.2f" % self.imposto)
            if self.restituicao and not self.desconto_completo_escolhido :
                #write simplificado a restituir
                declarando.write( "---\nCálculo Simplificado\nImposto a ser restituido (R$): %.2f" % self.imposto)
            if not self.restituicao and self.desconto_completo_escolhido :
                #write completo a pagar
                declarando.write( "---\nCálculo Completo\nImposto a pagar (R$): %.2f" % self.imposto)
            if self.restituicao and self.desconto_completo_escolhido :
                #write completo a restituir
                declarando.write( "---\nCálculo Completo\nImposto a ser restituído (R$): %.2f" % self.imposto)
                
            if self.restituicao :
                #write dados bancarios
                declarando.write('\n\nDados Bancários para restituição:\n\n%s\n\n' % self.declaracao[5][0].mostra_dados( ))
            
                          
            declarando.write( "-----------\n" )
          
            declarando.close()

            print ('\nDeclaração emitida com sucesso. (Nome do arquivo: %s)' % nome_declaracao)
