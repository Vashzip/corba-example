import sys

from omniORB import CORBA

import Sistema
import Sistema__POA


# --- A Implementação Real da Calculadora ---
class CalculadoraImpl(Sistema__POA.Calculadora):
    def quadrado(self, numero):
        resultado = numero * numero
        print(f" [Servidor] Recebi {numero}, devolvendo {resultado}")
        return resultado


# --- Configuração do CORBA ---
# 1. Inicia o ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poa._get_the_POAManager().activate()

# 2. Cria a instância da calculadora
servant = CalculadoraImpl()
obj_ref = servant._this()

# 3. Transforma o objeto em uma string (IOR) e salva no arquivo
ior = orb.object_to_string(obj_ref)

with open("servidor.ior", "w") as f:
    f.write(ior)

print(" [x] Servidor CORBA rodando!")
print(" [x] Endereço salvo em 'servidor.ior'.")
print(" [x] Pressione CTRL+C para encerrar.")

# 4. Mantém o servidor rodando
orb.run()
