import os
import subprocess
import time
from datetime import datetime

# Parâmetros base
start_range = int("41000000000000000", 16)
end_range = int("7ffffffffffffffff", 16)

total_subranges = 113211
address = "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9"
log_file = f"67-Sequencial-{total_subranges}.tsv"
output_file = "FOUNDFOUNDFOUND.txt"

# Função para calcular o tamanho de cada subrange
def calcular_subranges():
    subrange_size = (end_range - start_range) // total_subranges
    subranges = []
    for i in range(total_subranges):
        subrange_start = start_range + i * subrange_size
        subrange_end = subrange_start + subrange_size - 1
        if i == total_subranges - 1:  # Corrige o último range para o limite máximo
            subrange_end = end_range
        subranges.append((hex(subrange_start)[2:], hex(subrange_end)[2:]))
    return subranges

# Função para salvar os subranges em um arquivo .tsv
def salvar_subranges(subranges):
    with open(log_file, 'w') as f:
        f.write("Timestamp\tSubrange_Start\tSubrange_End\tStatus\n")
        for subrange in subranges:
            f.write(f"Not Scanned\t{subrange[0]}\t{subrange[1]}\tPending\n")

# Função para carregar os subranges do arquivo e filtrar os não escaneados
def carregar_subranges():
    subranges = []
    with open(log_file, 'r') as f:
        lines = f.readlines()[1:]  # Ignora o cabeçalho
        for line in lines:
            timestamp, subrange_start, subrange_end, status = line.strip().split("\t")
            if status == "Pending":
                subranges.append((subrange_start, subrange_end))
    return subranges

# Função para atualizar o status de um subrange no arquivo
def atualizar_status(subrange_start, subrange_end, status):
    lines = []
    with open(log_file, 'r') as f:
        lines = f.readlines()
    with open(log_file, 'w') as f:
        for line in lines:
            if subrange_start in line and subrange_end in line:
                f.write(f"{datetime.now()}\t{subrange_start}\t{subrange_end}\t{status}\n")
            else:
                f.write(line)

# Função para executar o KeyHunt
def executar_keyhunt(subrange_start, subrange_end):
    comando = [
        "./KeyHunt", "--gpu", "-m", "address", address,
        "--range", f"{subrange_start}:{subrange_end}",
        "--coin", "BTC", "-o", output_file,
    ]
    processo = subprocess.Popen(comando)
    return processo

# Função principal
def gerenciar_busca():
    try:
        subranges = carregar_subranges()
        total_restantes = len(subranges)
        total_escaneados = total_subranges - total_restantes

        print(f"Total de subranges: {total_subranges}")
        print(f"Subranges escaneados: {total_escaneados}")
        print(f"Subranges restantes: {total_restantes}")

        for subrange in subranges:
            subrange_start, subrange_end = subrange

            print(f"Escaneando subrange {subrange_start}:{subrange_end}")
            atualizar_status(subrange_start, subrange_end, "Scanning")

            processo = executar_keyhunt(subrange_start, subrange_end)

            # Aguarda 30 segundos, então mata o processo e atualiza o status
            time.sleep(30)
            processo.terminate()
            processo.wait()

            # Aguarda 2 segundo antes de prosseguir para o próximo subrange
            time.sleep(2)

            print(f"Subrange {subrange_start}:{subrange_end} finalizado.")
            atualizar_status(subrange_start, subrange_end, "Scanned")

            # Atualiza os contadores
            total_restantes -= 1
            total_escaneados += 1
            print(f"Progresso: {total_escaneados}/{total_subranges} subranges escaneados.")

        print("Todos os subranges foram escaneados.")

    except KeyboardInterrupt:
        print("\nEncerrando, aguarde...")
        time.sleep(2)
        print("Processo interrompido com sucesso.")

if __name__ == "__main__":
    if not os.path.exists(log_file):  # Gera os subranges apenas se o arquivo não existir
        subranges = calcular_subranges()
        salvar_subranges(subranges)
        print(f"Arquivo {log_file} criado com {total_subranges} subranges.")
    else:
        print(f"Arquivo {log_file} encontrado. Carregando subranges pendentes...")
    gerenciar_busca()
