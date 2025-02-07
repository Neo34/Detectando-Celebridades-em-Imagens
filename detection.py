import boto3

def identificar_celebridades(caminho_imagem):
    # Cria o cliente do Rekognition
    rekognition = boto3.client('rekognition', region_name='us-east-1')  # Verifique a região que suporta o serviço

    # Lê a imagem em modo binário
    with open(caminho_imagem, 'rb') as imagem:
        conteudo_imagem = imagem.read()

    # Chama a API recognize_celebrities
    resposta = rekognition.recognize_celebrities(Image={'Bytes': conteudo_imagem})

    # Processa e exibe os resultados
    if resposta.get('CelebrityFaces'):
        print("Celebridades reconhecidas na imagem:")
        for celebridade in resposta['CelebrityFaces']:
            nome = celebridade.get('Name', 'Nome não disponível')
            confiança = celebridade.get('MatchConfidence', 0)
            urls = celebridade.get('Urls', [])
            print(f"\nNome: {nome}")
            print(f"Confiança: {confiança:.2f}%")
            if urls:
                print("URLs de referência:")
                for url in urls:
                    print(f" - {url}")
    else:
        print("Nenhuma celebridade foi reconhecida na imagem.")

    # Caso deseje verificar os rostos não reconhecidos como celebridades:
    if resposta.get('UnrecognizedFaces'):
        print(f"\nQuantidade de rostos não reconhecidos como celebridades: {len(resposta['UnrecognizedFaces'])}")

# Exemplo de uso
if __name__ == "__main__":
    caminho_para_imagem = 'caminho/para/sua_imagem.jpg'  # Substitua pelo caminho da imagem que deseja analisar
    identificar_celebridades(caminho_para_imagem)
