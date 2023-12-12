# Atualizando nomes
key_mapping = {'Nome do Item' : 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
key_mapping


new_dados_csv = []

for old_dict in dados_csv:
    dict_temp = {}
    for old_key , value in old_dict.items():
        dict_temp[key_mapping[old_key]] = value
    new_dados_csv.append(dict_temp)
new_dados_csv[0] 

{'Nome do Produto': 'Lápis de sobrancelha',
 'Categoria do Produto': 'Roupas',
 'Preço do Produto (R$)': '55.17',
 'Quantidade em Estoque': '62',
 'Filial': 'Filial 1',
 'Data da Venda': '2023-04-13 18:58:06.794203'}
