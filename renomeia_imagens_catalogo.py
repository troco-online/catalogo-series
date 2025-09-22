import os
import json
import unicodedata

def normalizar_nome(nome):
    # Remove acentos e deixa tudo minúsculo
    return unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII').lower()

# Caminhos
CATALOGO = 'catalogo.json'
PASTA_IMAGENS = 'imagens'

# Carrega o catálogo
with open(CATALOGO, encoding='utf-8') as f:
    catalogo = json.load(f)

# Lista todos os arquivos da pasta de imagens
arquivos_imagens = os.listdir(PASTA_IMAGENS)

# Cria um dicionário de nomes normalizados para o nome real do arquivo
mapa_imagens = {normalizar_nome(nome): nome for nome in arquivos_imagens}

renomeados = []
nao_encontrados = []

for item in catalogo:
    nome_catalogo = item.get('imagem')
    if not nome_catalogo:
        continue
    nome_normalizado = normalizar_nome(nome_catalogo)
    if nome_normalizado in mapa_imagens:
        nome_arquivo_atual = mapa_imagens[nome_normalizado]
        if nome_arquivo_atual != nome_catalogo:
            # Renomeia o arquivo
            origem = os.path.join(PASTA_IMAGENS, nome_arquivo_atual)
            destino = os.path.join(PASTA_IMAGENS, nome_catalogo)
            print(f'Renomeando: {nome_arquivo_atual} -> {nome_catalogo}')
            os.rename(origem, destino)
            renomeados.append((nome_arquivo_atual, nome_catalogo))
    else:
        nao_encontrados.append(nome_catalogo)

print(f'Arquivos renomeados: {len(renomeados)}')
if nao_encontrados:
    print('Imagens não encontradas na pasta:')
    for nome in nao_encontrados:
        print('-', nome)
else:
    print('Todas as imagens do catálogo foram encontradas na pasta.')
