# Sistema Distribuído com CORBA (Python + omniORB)

Este projeto implementa um sistema de objetos distribuídos utilizando o padrão **CORBA** (Common Object Request Broker Architecture).

A implementação utiliza a linguagem **Python** através da biblioteca **omniORB**. O mecanismo de descoberta de serviços foi simplificado utilizando **Arquivos IOR** (Interoperable Object Reference), eliminando a necessidade de configurar e manter um serviço de nomes (Naming Service) externo.

## 📋 Pré-requisitos

* **Sistema Operacional:** Linux (Fedora, Ubuntu, Debian) ou WSL (Windows Subsystem for Linux).
* **Gerenciador de Pacotes:** Conda (Anaconda ou Miniconda).

## 🚀 Configuração do Ambiente (Conda)

Para garantir a compatibilidade das bibliotecas C++ do omniORB, utilizamos um ambiente Conda isolado.

1.  **Crie o ambiente virtual (Recomendado Python 3.10):**
    ```bash
    conda create -n corba_env python=3.10 -y
    ```

2.  **Ative o ambiente:**
    ```bash
    conda activate corba_env
    ```

3.  **Instale as dependências:**
    É necessário utilizar o canal `conda-forge` para obter os pacotes corretos (`omniorb` backend e `omniorbpy` bindings).
    ```bash
    conda install -c conda-forge omniorb omniorbpy -y
    ```

## 📂 Estrutura do Projeto

* `sistema.idl`: Definição da interface (contrato) do sistema distribuído.
* `server.py`: Implementação do servidor (Skeleton) que processa as requisições.
* `client.py`: Implementação do cliente (Stub) que consome o serviço remoto.
* `servidor.ior`: Arquivo gerado automaticamente contendo o endereço do objeto remoto.
* `Sistema/`: (Gerado automaticamente) Pacote Python contendo os Stubs gerados pelo compilador IDL.

## 🛠️ Passo a Passo para Execução

Abra dois terminais na pasta do projeto. Certifique-se de que o ambiente Conda esteja ativo em ambos:
```bash
conda activate corba_env
