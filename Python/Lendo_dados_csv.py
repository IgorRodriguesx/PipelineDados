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
  
  
