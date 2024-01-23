import json
import csv

# Funções
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
        return dados_json

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

def rename_columns(dados, key_mapping):
    new_dados_csv = []
    
    # Para cada registro na variável dados_csv
    for old_dict in dados_csv:
        dict_temp = {}
        for old_key , value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
            new_dados_csv.append(dict_temp)

    return new_dados_csv

def size_data(dados):
    return len(dados)

def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

# Puxando os locais dos arquivos
path_json = 'projeto_Requests/data_raw/dados_empresaA.json'
path_csv = 'projeto_Requests/data_raw/dados_empresaB.csv'

# Leitura dos dados Json
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f"Nome colunas dados json: {nome_colunas_json}")
print(f"tamanho dos dados json:{tamanho_dados_json}")

# Leitura dos dados Csv
dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f"Nome colunas dados csv: {nome_colunas_csv}")
print(f"tamanho dos dados json:{tamanho_dados_csv}")

# Transformação dos dados

key_mapping = {'Nome do Item' : 'Nome do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Classificação do Produto': 'Categoria do Produto',
                 'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

dados_fusao = join(dados_json, dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(nome_colunas_fusao)
print(tamanho_dados_fusao)
