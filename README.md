# Aula18.2 - DESAFIO: Criando Um Pacote de Calculadora

Este projeto consiste em uma calculadora simples em Python que realiza operações básicas como soma, subtração, multiplicação e divisão. A calculadora é modular, o que facilita a manutenção e a expansão futura.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

Aula18.2-DESAFIO-CriandoUmPacote/
│
├── __init__.py         # Torna o diretório um pacote Python
├── main.py             # Módulo principal que fornece a interface do usuário
├── basic_operations/   # Módulo para operações básicas
│   ├── __init__.py
│   ├── add.py          # Implementa a classe Sum e a função de adição
│   ├── subtract.py     # Implementa a classe Subtract e a função de subtração
│   ├── multiply.py     # Implementa a classe Multiply e a função de multiplicação
│   └── divide.py       # Implementa a classe Divide e a função de divisão

## Funcionalidades

A calculadora oferece as seguintes operações:

- __Soma__: Adiciona um conjunto de números.

- __Subtração__: Subtrai um conjunto de números.

- __Multiplicação__: Multiplica um conjunto de números.

- __Divisão:__ Divide dois números.

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/irbaeza/desafio-criando-um-pacote-de-calculadora.git
   ```

2. Execute o arquivo principal:

   ```bash
   python main.py
   ```

3. Siga as instruções exibidas no console para realizar as operações desejadas.

## Dependências

Este projeto não possui dependências externas necessárias para sua execução.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou solicitar recursos. Para contribuir, faça um fork do repositório, crie uma branch para sua funcionalidade ou correção e envie um pull request.

## Licença

Este projeto é de uso pessoal e não possui uma licença formal. Se você usar ou modificar este projeto, considere dar os devidos créditos.
