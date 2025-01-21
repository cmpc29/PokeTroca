# National Dex

Este repositório contém o código-fonte de um sistema de redes desenvolvido em Python que utiliza sockets para permitir a coleta de informações sobre Pokémon entre clientes em computadores distintos conectados à um servidor por uma mesma rede.

O projeto foi desenvolvido com o objetivo de aplicar conceitos de Redes de Computadores, como comunicação cliente-servidor, a elaboração de um novo protocolo de transporte e análise desses dados usando a plataforma WireShark.  

## Objetivo do Projeto
Criar uma aplicação simples e funcional para simular um sistema de troca de Pokémon, em que:
1. Os treinadores podem conectar seus computadores a um servidor central na mesma rede.
2. Cada treinador pode capturar um pokémon e solicitar informações sobre ele do servidor externo.
3. A troca de informações ocorre de maneira confiável, utilizando comunicação TCP e sockets para transmissão de dados.

## Funcionalidades  
- **Interface do usuário no terminal**: Interface simples e eficiente para capturar Pokémon e solicitar informações sobre eles do servidor.
- **Servidor centralizado**: Pode coordenar conexões com qualquer IP e compartilhar suas informações.
- **Robustez**: Programa preparado com mensagens de erro customizadas para lidar com diversos tipos de entradas equivocadas.
- **Confiabilidade**: Garantia de chegada da informação entre servidor <-> cliente por meio de conexão TCP.
- **Time Out**: Manutenção da conectividade por meio de timers. Reconecta usuários automaticamente à seção previamente expirada, dentro de uma faixa de tempo.

## Tecnologias Utilizadas  
- Linguagem de programação: **Python 3.13**  
- Biblioteca de redes: **socket**
- Banco de dados local: **sqlite**
- Demais bibliotecas: **requests** e **threading** 
- Ambiente de desenvolvimento: VSCode

## Como Funciona?
1. **Clientes**: Cada treinador executa cliente/main.py em seu computador, conectando-se com o servidor pelo IP do servidor {HOST} e porta especificada {PORT}.
2. **Servidor**: O servidor pode visualizar quais treinadores estão conectados e verificar quais Pokémon eles desejam coletar informações. Envia automaticamente as informações requeridas.

## Contribuidores
- Caio Merçon (https://github.com/cmpc29)
- Marcelo Rodrigues (https://github.com/marcelo-mrodrigues)
- Pedro Daniel Bomtempo Medeiros (https://github.com/Pedro-Daniel)
