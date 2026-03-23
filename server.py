from socket import *
from constCS import *

def apply_operation(op, value):
    try:
        value = float(value)

        if op == "c_to_f":
            return (value * 9/5) + 32

        elif op == "f_to_c":
            return (value - 32) * 5/9

        elif op == "km_to_miles":
            return value * 0.621371

        elif op == "miles_to_km":
            return value / 0.621371

        elif op == "kg_to_lb":
            return value * 2.20462

        elif op == "lb_to_kg":
            return value / 2.20462

        else:
            return "Erro: operação desconhecida"

    except:
        return "Erro: valor inválido"


def process_request(data):
    try:
        parts = data.split("|")
        if data.startswith("exit"):
            return "Encerrando conexão..."
        if len(parts) < 2:
            return "Erro: formato inválido"

        ops = parts[0].split(",")
        value = parts[1]

        result = value

        for op in ops:
            result = apply_operation(op.strip(), result)

            if isinstance(result, str) and "Erro" in result:
                break

        return str(result)

    except:
        return "Erro no processamento"


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Servidor aguardando conexão...")

(conn, addr) = s.accept()


while True:
    data = conn.recv(1024)
    if not data:
        break

    received = bytes.decode(data)
    print("Recebido:", received)

    if received.startswith("exit"):
        conn.send(str.encode("Conexão encerrada"))
        break

    response = process_request(received)

    conn.send(str.encode(response))

conn.close()
