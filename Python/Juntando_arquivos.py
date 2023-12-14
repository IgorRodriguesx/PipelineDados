# verificando quantidade em cada uma das variáveis
len(dados_json)
3123
len(new_dados_csv)
1323

# somando a junção dos dados
len(dados_json + new_dados_csv)
4446


# criando nova variável com lista vazia
combined_list = []
# métdo .extend recebendo lista dos dados_json
combined_list.extend(dados_json)
# recebendo também a lista dos new_dados_json
combined_list.extend(new_dados_csv)

# verificando como ficou a nová varialvel que recebeu os dados dos dois arquivos
len(combined_list)
4446
