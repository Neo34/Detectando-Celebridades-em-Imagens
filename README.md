# Detectando-Celebridades-em-Imagens

Considerações Adicionais
Imagens Armazenadas no S3:
Caso sua imagem esteja armazenada em um bucket S3, você pode passar a referência da imagem desta forma:

response = rekognition.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': 'nome-do-seu-bucket',
            'Name': 'caminho/para/sua_imagem.jpg'
        }
    }
)

