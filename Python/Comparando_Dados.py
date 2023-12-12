# Método .keys() utilizado para visualizar as chaves no dicionário
# Atribuindo uma variável e analisando dados Json
nome_colunas_json = list(dados_json[0].keys())
nome_colunas_json
['Nome do Produto',
 'Categoria do Produto',
 'Preço do Produto (R$)',
 'Quantidade em Estoque',
 'Filial']

# Leitura de colunas json usando o Len
len(nome_colunas_json)
5

# Atribuindo uma variável e analisando dados csv
nome_colunas_csv = list(dados_csv[0].keys())
nome_colunas_csv
['Nome do Item',
 'Classificação do Produto',
 'Valor em Reais (R$)',
 'Quantidade em Estoque',
 'Nome da Loja',
 'Data da Venda']

# Leitura de colunas de csv usando o Len
len(nome_colunas_csv)
6

