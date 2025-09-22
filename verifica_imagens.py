import json
import os

# Caminho dos arquivos
CATALOGO = 'catalogo.json'
IMAGENS_DIR = 'imagens'

def normalizar_nome(nome):
    # Remove espaços extras e normaliza para comparação
    return nome.strip()

def main():
    with open(CATALOGO, encoding='utf-8') as f:
        catalogo = json.load(f)

    imagens_catalogo = set(normalizar_nome(item['imagem']) for item in catalogo if 'imagem' in item)
    imagens_pasta = set(normalizar_nome(os.path.join(IMAGENS_DIR, nome)) for nome in os.listdir(IMAGENS_DIR))

    # Checa imagens do catálogo que não existem na pasta
    faltando = sorted(img for img in imagens_catalogo if img not in imagens_pasta)
    # Checa imagens na pasta que não estão no catálogo
    sobrando = sorted(img for img in imagens_pasta if img not in imagens_catalogo)

    print('Imagens do catálogo que NÃO existem na pasta:')
    for img in faltando:
        print('  -', img)
    print('\nImagens na pasta que NÃO estão no catálogo:')
    for img in sobrando:
        print('  -', img)

if __name__ == '__main__':
    main()
