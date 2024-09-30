Desafio: Criando um sistema Bancário

Criar um sistema bancário com as seguintes operaçôes:
* Sacar
* Depositar 
* Visualizar Extrato

SACAR
O sistema deve permitir realizar apenas 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será 
possível sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

DEPOSITAR
Deve ser possível depositar apenas valores positivos na conta bancária. Para este projeto foi utilizado apenas 1 usuário,
dessa forma não precisamos inserir número da agência e conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.


EXTRATO
O extrato deve listar todos os depósitos e saques realizados na conta. 
No fim da listagem deve ser exibido o saldo atual da conta.
Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, 
Exemplo: 1500.45 = R$ 1500.45

