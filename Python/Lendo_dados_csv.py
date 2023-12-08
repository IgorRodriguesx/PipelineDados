path_csv = '../dados_raw/dados_empresaB.csv'
with open(path_csv , 'r') as file:
    print(file.readlines())

# Print nome das colunas
with open(path_csv , 'r') as file:
    print(file.readlines()[0])

# Valores referentes aos produtos
with open(path_csv , 'r') as file:
    print(file.readlines()[1])

# armazenando dados na variavel 'dados_csv'
with open(path_csv , 'r') as file:
    dados_csv = file.readlines()

# Importar para poder ler o CSv
import csv

# reader capaz de fazr leitura
with open(path_csv , 'r') as file:
    dados_csv = file.readlines()

# Fazer laço de repetição com o For para ler todas as linhas
with open(path_csv , 'r') as file:
    spamreader= csv.reader(file, delimiter=',')
    for row in spamreader:        # Dentro desse FOr , percorrer todos os valores que o spamreader puder assumir e ir atribuindo ao row
        print(row)
  
  
