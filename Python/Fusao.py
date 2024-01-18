import json
import csv

# Função
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
        return dados_json

 # Função   
def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv , 'r') as file:
        spamreader= csv.DictReader(file, delimiter=',')
        for row in spamreader:     
            dados_csv.append(row)    
    
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []
    # Condicional verificando tipo do arquivo
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)

    elif tipo_arquivo == 'json':
        dados = leitura_json(path)

    return dados    

# Puxando os locais dos arquivos
path_json = 'projeto_Requests/data_raw/dados_empresaA.json'
path_csv = 'projeto_Requests/data_raw/dados_empresaB.csv'

# Leitura dos dados Json e Csv
dados_json = leitura_dados(path_json, 'json')
print(dados_json[0])

dados_csv = leitura_dados(path_csv, 'csv')
print(dados_csv[0])
