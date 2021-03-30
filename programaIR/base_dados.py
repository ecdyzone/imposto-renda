# Programa alternativo de cálculo do imposto de renda versão 1

from sqlite3 import connect
from contribuinte import Contribuinte
from dependente import Dependente
from rendimento_tributavel import Rendimento_tributavel
from rendimento_exclusiva_definitiva import Rendimento_exclusiva_definitiva
from bem import Bem
from dados_bancario import Dados_bancario
from entrada import Texto
from cpf import CPF

# classe que contém e manipula a base de dados SQL que armazena a declaração
class Base_Dados :
    def __init__( self, nome ) :
        self.nome = nome
 
    # pede o nome do arquivo da declaração
    def pede_nome( self ) :
        while True :
            self.nome = Texto( "\nDigite o número do seu CPF: ", self.nome ).string.replace('.', '').replace(',', '').replace('-', '').replace(' ', '')
            valido = CPF(self.nome)
            if valido.isValid() == True :         # só muda se o cpf for válido
                if input( "Confirma que o CPF está correto? Não será possível alterá-lo depois. (S/N) ? " ).lower( ) != "s" :
                    continue
                else:
                    return
            print( "Entrada inválida, favor digitar um cpf válido" )
    
    # recupera uma declaração salva em um banco de dados SQL
    def recupera( self ) :
        self.pede_nome( )
        #declaracao[i], com i = 0 para contribuintes, i = 1 para dependentes... (como comentado em programaIR.py)
        #self.nome aqui serve pra passar o CPF introduzido pelo usuário no início do programa pra dentro de contribuinte.cpf (Ver linha 45 em menu.py)
        declaracao = [ [], [], [], [], [], [], self.nome ]  # lista de objetos da classe Declaracao a ser recuperada
        
        try :   # lê o arquivo apenas se ele existir
            nome_db = str(self.nome) + ".db"
            arquivo = open( nome_db, "r" )  # tenta abrir, se já existir
            arquivo.close( )    # fecha o arquivo para ler como base de dados
            conexao = connect( nome_db )
            cursor = conexao.cursor( )
            cursor.execute( "select * from declaracao" )  # seleciona todos os registros
            registros = cursor.fetchall( )  # lê todos os registros como lista de tuplas
            print ("\nDeclaração encontrada")    
            for linha in registros :
               
                if linha[0] != None :
                    declaracao[0].append( Contribuinte( linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]) ) # linha[3] é o cpf
                    
                elif linha[6] != None :
                    declaracao[1].append( Dependente (linha[6], linha[7], linha[8], linha[9] ) )
                    
                elif linha[10] != None :
                    declaracao[2].append( Rendimento_tributavel( linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16] ) )

                elif linha[17] != None :
                    declaracao[3].append( Rendimento_exclusiva_definitiva( linha[17], linha[18], linha[19], linha[20] ) )

                elif linha[21] != None :
                    declaracao[4].append( Bem( linha[21], linha[22], linha[23], linha[24] ) )

                elif linha[25] != None :
                    declaracao[5].append( Dados_bancario( linha[25], linha[26], linha[27], linha[28] ) )
                
            conexao.close( )
                                          
        except FileNotFoundError :
            print( "\nNão foi encontrada uma declaração já existente vinculada ao contribuinte de CPF igual a '%s'. \nPortanto, acaba de ser criada uma declaracao vazia." % self.nome )
        return declaracao
    
    # salva uma declaração em um banco de dados SQL, substituindo o anterior se existir
    def salva( self, declaracao ) :
        nome_db = str(self.nome) + ".db"
        conexao = connect( nome_db )  # se não existir ainda, cria base
        cursor = conexao.cursor( )
        cursor.execute( "drop table if exists declaracao" )  # apaga tabela existente
        cursor.execute( "create table declaracao ( nome text, nascimento text, endereço text, cpf text, telefone text, ocupaçao text, Tipo_dep text, Dependente text, Nascimento_dep text, CPF_dep text, CPF_CNPJ_da_fonte_pagadora_rt text, Nome_da_fonte_pagadora_rt text, Rendimento_recebido_de_PJ text, Contribuição_previdenciária_de_PJ text, Imposto_retido_na_fonte text, decimo_terceiro_salario text, IRRF_sobre_decimo_terceiro_salario text, Tipo_red text, CPF_CNPJ_da_fonte_pagadora_red text, Nome_da_fonte_pagadora_red text, Valor_do_rendimento text, Tipo_de_Bem text, Descrição text, Situaçao_2018 text, Situaçao_2019 text, Banco text, Agência text, Conta_Corrente text, DV text )" )

        for contribuinte in declaracao[0] :
            cursor.execute( "insert into declaracao ( nome, nascimento, endereço, cpf, telefone, ocupaçao ) values ( ?, ?, ?, ?, ?, ?)", ( contribuinte.nome, contribuinte.nascimento, contribuinte.endereço, contribuinte.cpf, contribuinte.telefone, contribuinte.ocupaçao ) )
        for dependente in declaracao[1] :
            cursor.execute( "insert into declaracao ( Tipo_dep, Dependente, Nascimento_dep, CPF_dep ) values (?, ?, ?, ?)", ( dependente.tipo, dependente.nome_dep, dependente.nascimento_dep, dependente.cpf_dep ) )
        for rendimento_tributavel in declaracao[2] :
            cursor.execute("insert into declaracao (CPF_CNPJ_da_fonte_pagadora_rt, Nome_da_fonte_pagadora_rt, Rendimento_recebido_de_PJ, Contribuição_previdenciária_de_PJ, Imposto_retido_na_fonte, decimo_terceiro_salario, IRRF_sobre_decimo_terceiro_salario) values ( ?, ?, ?, ?, ?, ?, ?)", ( rendimento_tributavel.cnpj_rt, rendimento_tributavel.nome_fonte_rt, rendimento_tributavel.rendimento_pj, rendimento_tributavel.prev, rendimento_tributavel.imposto, rendimento_tributavel.sal_13, rendimento_tributavel.ir_sal_13 ) )
        for rendimento_exclusiva_definitiva in declaracao[3] :
            cursor.execute("insert into declaracao ( Tipo_red, CPF_CNPJ_da_fonte_pagadora_red, Nome_da_fonte_pagadora_red, Valor_do_rendimento) values (?, ?, ?, ?)", ( rendimento_exclusiva_definitiva.tipo_red, rendimento_exclusiva_definitiva.cnpj_red, rendimento_exclusiva_definitiva.nome_fonte_red, rendimento_exclusiva_definitiva.rendimento_pj ) )
        for bem in declaracao[4] :
            cursor.execute("insert into declaracao ( Tipo_de_Bem, Descrição, Situaçao_2018, Situaçao_2019) values (?, ?, ?, ?)", ( bem.tipo_bem, bem.descrição, bem.situaçao_2018, bem.situaçao_2019 ))
        for dados_bancario in declaracao[5] :
            cursor.execute("insert into declaracao ( Banco, Agência, Conta_Corrente, DV) values (?, ?, ?, ?)", ( ( dados_bancario.banco, dados_bancario.agencia, dados_bancario.conta, dados_bancario.dv ) ))
            
            
        conexao.commit( )
        conexao.close( )

        print('\nDeclaração salva com sucesso!')


