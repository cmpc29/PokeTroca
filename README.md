# National Dex

Este repositório contém o código-fonte de um sistema de redes desenvolvido em Python que utiliza sockets para permitir a troca de diferentes Pokémon entre usuários em computadores distintos conectados à mesma rede.

O projeto foi desenvolvido com o objetivo de aplicar conceitos de redes de computadores, como comunicação cliente-servidor, a elaboração de um novo protocolo de transporte e análise desses dados usando a plataforma WireShark.  

## Objetivo do Projeto
Criar uma aplicação simples e funcional para simular um sistema de troca de Pokémon, em que:
1. Os jogadores podem conectar seus computadores a um servidor central na mesma rede.
2. Cada jogador pode oferecer um Pokémon para troca e visualizar os Pokémon disponíveis enviados por outros jogadores.
3. A troca ocorre de maneira segura e sincronizada, utilizando sockets para transmissão de dados.

## Funcionalidades  
- **Cliente Pokémon**: Interface simples para enviar Pokémon ao servidor e visualizar os Pokémon disponíveis.
- **Troca Sincronizada**: Garante que as trocas só ocorram após a aceitação de ambas as partes de maneira P2P.
- **Validação de dados**: Para evitar trocas inconsistentes ou corrompidas.

## Tecnologias Utilizadas  
- Linguagem de programação: **Python 3.13**  
- Biblioteca de redes: **socket**  
- Serialização de dados: **pickle**  
- Ambiente de desenvolvimento: VSCode

## Como Funciona?
1. **Clientes**: Cada jogador executa o cliente/servidor em seu computador, conectando-se entre si pelo IP e porta fornecidos.
2. **Trocas**: Os jogadores podem listar Pokémon, escolher parceiros de troca e concluir as transações.

## Contribuidores
- Caio Merçon
- Marcelo Rodrigues
- Pedro Daniel Bomtempo Medeiros
