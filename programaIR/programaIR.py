# Programa alternativo de cálculo do imposto de renda versão 1

from interface import Interface

# programa principal
Interface( "nome.db" )       # inicia interface com nome default do arquivo da agenda



'''
Explicação da estrutura de dados:

a declaração é uma lista de listas, definida na linha 35 de base_dados.py
inicializada na seguinte forma: declaracao = [ [], [], [], [] ,[], [] ]
ou seja, cada uma das sublistas agrupa objetos de uma classe.
declaracao[0] é para contribuintes
declaracao[1] é para dependentes
declaracao[2] é para rendimento_tributavel
declaracao[3] é para rendimento_exclusiva_definitiva
declaracao[4] é para bens
declaracao[5] é para dados bancarios

'''
