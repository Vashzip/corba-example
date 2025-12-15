import sys

from omniORB import CORBA

import Sistema

# 1. Inicia o ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

try:
    # 2. Lê o endereço do servidor do arquivo
    with open("servidor.ior", "r") as f:
        ior = f.read()

    # 3. Conecta ao objeto remoto
    obj = orb.string_to_object(ior)

    # 4. Faz o "cast" para garantir que é uma Calculadora
    calc = obj._narrow(Sistema.Calculadora)

    if calc is None:
        print("Erro: O objeto não é uma Calculadora válida.")
    else:
        # --- MUDANÇA AQUI: Input do Usuário ---
        while True:
            try:
                entrada = input(
                    "\nDigite um número para calcular o quadrado (ou 'sair' para fechar): "
                )

                if entrada.lower() == "sair":
                    print("Encerrando cliente.")
                    break

                # Converte o texto para número decimal (double)
                valor = float(entrada)

                print(f" [Cliente] Enviando {valor} para o servidor...")
                resultado = calc.quadrado(valor)
                print(f" [Cliente] Resultado recebido: {resultado}")

            except ValueError:
                print(" [!] Erro: Por favor, digite apenas números válidos (ex: 10.5).")

except FileNotFoundError:
    print(" [!] Erro: Arquivo 'servidor.ior' não encontrado.")
    print("     Rode o 'server.py' primeiro!")
except Exception as e:
    print(f" [!] Erro CORBA: {e}")
