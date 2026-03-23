from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite 'sair' para encerrar.")
print("""
Operações disponíveis:
- c_to_f
- f_to_c
- km_to_miles
- miles_to_km
- kg_to_lb
- lb_to_kg

Formato: op1|valor
""")

while True:
    msg = input(">>> ")

    if msg.lower() == "sair":
        s.send(str.encode("exit|"))
        break

    s.send(str.encode(msg))

    data = s.recv(1024)

    print("Resposta:", bytes.decode(data))

s.close()
