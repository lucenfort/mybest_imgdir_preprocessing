import os
import shutil
from PIL import Image
from compress import compress
from resize import resize

# Diretório de entrada
input_dir = "original_images"
# Diretório de saída
output_dir = "compressed_images"

# Criar o diretório de saída, se ele não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Percorrer todas as pastas e imagens no diretório de entrada
for root, dirs, files in os.walk(input_dir):
    for dir in dirs:
        # Criar a mesma estrutura de pastas no diretório de saída
        output_subdir = os.path.join(output_dir, dir)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)
    for file in files:
        # Ignorar arquivos que não sejam imagens
        if not file.endswith(".jpg") and not file.endswith(".png"):
            continue
        # Carregar a imagem
        image_path = os.path.join(root, file)
        image = Image.open(image_path)
        # Comprimir a imagem
        compressed_image = compress(image)
        # Redimensionar a imagem comprimida
        resized_image = resize(compressed_image, (256, 256))
        # Criar o caminho de saída
        output_path = os.path.join(output_dir, image_path[len(input_dir):])
        # Salvar a imagem redimensionada
        resized_image.save(output_path)
