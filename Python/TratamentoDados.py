# Sobrescrevendo a variavel para ser combined_list acessando o ultimo valor (-1) onde estão os arquivos CSV com a data da compra pedindo as chaves .keys , tudo isso dentro de uma lista (list) 
# Atualizar o nome da coluna com o nome da compra
nomes_colunas = list(combined_list[-1].keys())
nomes_colunas
# Pegou o ultimo registro da lista combinada e adicionou na variavel sobrescrita

# ANTES
    ['Nome do Produto',
 'Categoria do Produto',
 'Preço do Produto (R$)',
 'Quantidade em Estoque',
 'Filial']

# DEPOIS                             
['Nome do Produto',
 'Categoria do Produto',
 'Preço do Produto (R$)',
 'Quantidade em Estoque',
 'Filial', 
 'Data da Venda']



# lista de listas
# Primeiro registro será o nome das colunas
dados_combinados_tabela = [nomes_colunas]

# trazendo dados da variavel combined_list
for row in combined_list:
    # Zerando a linha
    linha = []
    # Criando a lista novamente
    for coluna in nomes_colunas:
        linha.append(row.get(coluna, 'Indisponível'))
    dados_combinados_tabela.append(linha)    


# TRANSFORMADA OS DADOS EM UMA LISTA DE LISTAS (TABELA) PARA SALVAR NO MOLDE CSV



