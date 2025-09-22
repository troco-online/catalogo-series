import os
import json
import unicodedata

def normalizar_nome(nome):
    # Remove acentos e deixa tudo minúsculo
    return unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII').lower()

CATALOGO = 'catalogo.json'
PASTA_IMAGENS = 'imagens'

with open(CATALOGO, encoding='utf-8') as f:
    catalogo = json.load(f)

arquivos_imagens = os.listdir(PASTA_IMAGENS)
mapa_imagens = {normalizar_nome(os.path.splitext(nome)[0]): nome for nome in arquivos_imagens}

renomeados = []
nao_encontrados = []

for item in catalogo:
    nome = item.get('nome')
    imagem_atual = item.get('imagem')
    if not nome or not imagem_atual:
        continue
    # Pega extensão da imagem atual
    ext = os.path.splitext(imagem_atual)[1]
    nome_normalizado = normalizar_nome(os.path.splitext(os.path.basename(imagem_atual))[0])
    # Procura imagem correspondente
    if nome_normalizado in mapa_imagens:
        nome_arquivo_atual = mapa_imagens[nome_normalizado]
        novo_nome_arquivo = nome.strip() + ext
        novo_caminho = os.path.join(PASTA_IMAGENS, novo_nome_arquivo)
        origem = os.path.join(PASTA_IMAGENS, nome_arquivo_atual)
        if origem != novo_caminho:
            if not os.path.exists(novo_caminho):
                try:
                    # Se só muda o case, faz rename para um nome temporário antes
                    if nome_arquivo_atual.lower() == novo_nome_arquivo.lower() and nome_arquivo_atual != novo_nome_arquivo:
                        temp_nome = novo_nome_arquivo + '.tmp'
                        temp_caminho = os.path.join(PASTA_IMAGENS, temp_nome)
                        os.rename(origem, temp_caminho)
                        os.rename(temp_caminho, novo_caminho)
                    else:
                        os.rename(origem, novo_caminho)
                    print(f'Renomeando: {nome_arquivo_atual} -> {novo_nome_arquivo}')
                    renomeados.append((nome_arquivo_atual, novo_nome_arquivo))
                except Exception as e:
                    print(f'Erro ao renomear {nome_arquivo_atual} -> {novo_nome_arquivo}: {e}')
            else:
                print(f'Arquivo já existe: {novo_nome_arquivo}, pulando...')
            # Atualiza o campo imagem no catálogo
            item['imagem'] = f"imagens/{novo_nome_arquivo}"
        else:
            # Já está com o nome correto
            item['imagem'] = f"imagens/{novo_nome_arquivo}"
    else:
        nao_encontrados.append(imagem_atual)

# Salva o catálogo atualizado
with open(CATALOGO, 'w', encoding='utf-8') as f:
    json.dump(catalogo, f, ensure_ascii=False, indent=4)

print(f'Arquivos renomeados: {len(renomeados)}')
if nao_encontrados:
    print('Imagens não encontradas na pasta:')
    for nome in nao_encontrados:
        print('-', nome)
else:
    print('Todas as imagens do catálogo foram renomeadas conforme o campo "nome".')
