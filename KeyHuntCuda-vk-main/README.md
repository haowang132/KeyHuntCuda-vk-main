# KeyHuntCuda - vk

--------------------------------------------------------------------------------------------------------------------




#Tutorial: Instalação e Uso do Código



1 - Install libgm
````
apt update && apt upgrade
apt install git -y
apt install build-essential -y
apt install libssl-dev -y
apt install libgmp-dev -y

````
2 - Cuda 12.6
````
wget https://developer.download.nvidia.com/compute/cuda/12.6.3/local_installers/cuda_12.6.3_560.35.05_linux.run
sudo sh cuda_12.6.3_560.35.05_linux.run

````
3 - Python 
````
sudo apt-get install python3.9
````
4 - Clonar o repositório
````
git clone https://github.com/vkThiago/KeyHuntCuda-vk.git
````

5 - Instalação com placa de video
````
cd KeyHuntCuda-vk
make gpu=1 CCAP=75 all
````
Instalação sem placa de video
````
cd KeyHuntCuda-vk
make all
````
O CCAP deve ser de acordo com a sua placa, segue abaixo uma lista com os principais modelos e o seu CCAP relativo.
````
Arquitetura Ampere (mais recente para desktops e data centers):
NVIDIA RTX 4090 – Compute Capability: 89
NVIDIA RTX 4080 – Compute Capability: 89
NVIDIA RTX 4070 Ti – Compute Capability: 89
NVIDIA RTX 4060 – Compute Capability: 89
NVIDIA A100 – Compute Capability: 80
NVIDIA A40 – Compute Capability: 86
NVIDIA A30 – Compute Capability: 80
NVIDIA A10 – Compute Capability: 86
NVIDIA A100 Tensor Core – Compute Capability: 80
Arquitetura Turing:
NVIDIA RTX 3090 – Compute Capability: 86
NVIDIA RTX 3080 – Compute Capability: 86
NVIDIA RTX 3070 – Compute Capability: 86
NVIDIA RTX 2080 Ti – Compute Capability: 75
NVIDIA RTX 2080 Super – Compute Capability: 75
NVIDIA RTX 2070 Super – Compute Capability: 75
NVIDIA RTX 2060 Super – Compute Capability: 75
NVIDIA RTX 1660 – Compute Capability: 75
NVIDIA RTX 1650 – Compute Capability: 75
NVIDIA TITAN RTX – Compute Capability: 75
Arquitetura Volta:
NVIDIA Titan V – Compute Capability: 70
NVIDIA V100 Tensor Core – Compute Capability: 70
Arquitetura Pascal:
NVIDIA GTX 1080 Ti – Compute Capability: 61
NVIDIA GTX 1080 – Compute Capability: 61
NVIDIA GTX 1070 – Compute Capability: 61
NVIDIA Tesla P100 – Compute Capability: 60
NVIDIA GTX Titan X (Pascal) – Compute Capability: 61
````

----------------------------------------------------------------------------------------------------------------------------------

Após instalar basta rodar o comando:

````
python3 novo-67.py
````
