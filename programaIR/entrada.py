# Programa alternativo de cálculo do imposto de renda versão 1

# classes genéricas para entrada de dados para todas as classes específicas   
      
# classe para entrada de valor inteiro válido pelo usuário
class Inteiro :
    def __init__( self, pergunta, inicio, fim ) :
        while True :
            try :               # garante que a entrada seja um número inteiro
                self.valor = int( input( pergunta ) )
                if inicio <= self.valor <= fim :
                    return
            except ValueError :
                print( "Valor inválido, favor digitar entre %d e %d" % ( inicio, fim ) )


# classe para entrada de texto (string) não vazio pelo usuário (com valor padrão opcional)
class Texto :
    def __init__( self, pergunta, padrao = "" ) :
        while True :
            self.string = input( pergunta )
            if self.string != "" :
                return
            elif padrao != "" :
                self.string = padrao
                return
            print( "Entrada inválida, favor digitar pelo menos um caractere" )

# classe para entrada de valor real positivo
class Real :
    def __init__( self, pergunta, é_inteiro = '' ) :
        while True :
            try :
                if é_inteiro == 'inteiro':
                    self.numero = int( (input( pergunta )).replace('.', '').replace(',', '').replace('-', '').replace(' ', '') )
                else:
                    self.numero = float( input( pergunta ) )
                if self.numero >= 0 :
                    return
            except ValueError :   
                print( "Entrada inválida, favor digitar um número positivo." )
            
