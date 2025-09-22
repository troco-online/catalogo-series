import json

CATALOGO = 'catalogo.json'

with open(CATALOGO, encoding='utf-8') as f:
    catalogo = json.load(f)

for item in catalogo:
    nome = item.get('nome')
    if nome:
        item['imagem'] = f"imagens/{nome}.jpg"

with open(CATALOGO, 'w', encoding='utf-8') as f:
    json.dump(catalogo, f, ensure_ascii=False, indent=4)

print('Todos os campos "imagem" foram atualizados para o padrão: imagens/NOME.jpg')
