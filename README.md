[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.
#Descrição do Sistema

O servidor oferece operações de conversão de unidades, que podem ser solicitadas pelo cliente através de mensagens enviadas pela rede.

O cliente envia uma requisição com a operação desejada e um valor numérico, e o servidor processa essa requisição e retorna o resultado.

##Operações
O servidor suporta as seguintes conversões:
c_to_f – Celsius → Fahrenheit
f_to_c – Fahrenheit → Celsius
km_to_miles – Quilômetros → Milhas
miles_to_km – Milhas → Quilômetros
kg_to_lb – Quilogramas → Libras
lb_to_kg – Libras → Quilogramas
