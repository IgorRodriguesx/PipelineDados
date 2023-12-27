nomes_colunas = list(combined_list[0].keys())
nomes_colunas

path_dados_combinados = '../data_processed/dados_combinados.csv'

# w de write para entrar no modo de escrita
with open(path_dados_combinados, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=nomes_colunas) #fieldnames=cabeçalho
    writer.writeheader() # Escrevendo os cabeçalhos

    # for para passar em cada linha na variável combined_list
    for row in combined_list:
        writer.writerow(row) #Escrevendo em cada linha
