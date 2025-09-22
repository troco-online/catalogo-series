import json
import os

CATALOGO = 'catalogo.json'
IMAGENS_DIR = 'imagens'

# Gera um dicionário de nomes normalizados para nomes reais
imagens_pasta = {nome.lower().strip(): nome for nome in os.listdir(IMAGENS_DIR)}

with open(CATALOGO, encoding='utf-8') as f:
    catalogo = json.load(f)

corrigidos = 0
for item in catalogo:
    if 'imagem' in item:
        nome_atual = item['imagem']
        nome_normalizado = nome_atual.replace('imagens/','').lower().strip()
        if nome_normalizado in imagens_pasta:
            nome_correto = imagens_pasta[nome_normalizado]
            caminho_correto = f"imagens/{nome_correto}"
            if nome_atual != caminho_correto:
                item['imagem'] = caminho_correto
                corrigidos += 1

if corrigidos:
    with open(CATALOGO, 'w', encoding='utf-8') as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=2)
    print(f"Corrigidos {corrigidos} caminhos de imagem no catalogo.json!")
else:
    print("Nenhuma correção necessária. Todos os caminhos já estão corretos.")
