import os
import subprocess
import shutil
from tqdm import tqdm

def converter_ts_para_mp4(origem, destino):
    # Verifica se a pasta MP4 existe na pasta de origem, se não, cria ela
    pasta_mp4 = os.path.join(origem, "mp4_result")
    if not os.path.exists(pasta_mp4):
        os.makedirs(pasta_mp4)
    
    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(origem)
    
    for arquivo in tqdm(arquivos, desc="Converting files", unit="file"):
        if arquivo.endswith(".ts"):
            caminho_arquivo = os.path.join(origem, arquivo)
            nome_arquivo_sem_extensao = os.path.splitext(arquivo)[0]
            arquivo_mp4 = nome_arquivo_sem_extensao + ".mp4"
            caminho_arquivo_mp4 = os.path.join(pasta_mp4, arquivo_mp4)
            
            # Comando ffmpeg para conversão
            comando_ffmpeg = f'ffmpeg -i "{caminho_arquivo}" -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k "{caminho_arquivo_mp4}"'
            
            # Executa o comando ffmpeg e captura a saída em tempo real
            process = subprocess.Popen(
                comando_ffmpeg,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            
            # Espera até que a conversão seja concluída
            process.wait()
    
    print("Conversão concluída.")

# Define a pasta de origem como o diretório atual + "sample"
pasta_origem = os.path.join(os.getcwd(), "sample")

# Define o destino como o diretório atual + "sample" + "mp4result"
pasta_destino = os.path.join(os.getcwd(), "sample", "mp4result")

# Verifica se a pasta de destino existe, caso contrário, cria
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Copia todos os arquivos da pasta de origem para a pasta de destino
for arquivo in os.listdir(pasta_origem):
    if os.path.isfile(os.path.join(pasta_origem, arquivo)):  # Verifica se é um arquivo
        shutil.copy(os.path.join(pasta_origem, arquivo), pasta_destino)
    
converter_ts_para_mp4(pasta_origem, pasta_destino)
