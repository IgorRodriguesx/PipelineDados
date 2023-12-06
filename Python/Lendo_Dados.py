path_json = '../data_raw/dados_empresaA.json'

# Função Open para abrir os arquivos # Parametro para ler arquivo > path_json # 'r' de Read apenas para ler # As > 'apelido' para ler o arquivo # Armazenado na variavel File

with open(path_json, 'r') as file:
    print(file.readline())           # > Leitura dos dados .Json 

# Salvou os dados na variável 'dados'

with open(path_json, 'r') as file:
    dados = file.readline()   
