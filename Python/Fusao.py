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

def get_columns(dados):
    return list(dados[0].keys())


# Puxando os locais dos arquivos
path_json = 'projeto_Requests/data_raw/dados_empresaA.json'
path_csv = 'projeto_Requests/data_raw/dados_empresaB.csv'

# Leitura dos dados Json e Csv
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
print(nome_colunas_json)

dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

key_mapping = {'Nome do Item' : 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

# Transformação dos dados

def rename_columns(dados, key_mapping):
    new_dados_csv = []
    
    # Para cada registro na variável dados_csv
    for old_dict in dados_csv:
        dict_temp = {}
        for old_key , value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.[0]
