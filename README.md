# 🍽️ Sistema de Gerenciamento de Restaurante (Console)

Este projeto é um sistema simples de gerenciamento para restaurantes, feito em Python com interface de texto no console. Ele permite controlar o **estoque**, **cardápio**, **mesas**, **pedidos**, **pagamentos** e **relatórios de vendas**.

## ⚙️ Funcionalidades

### 🛒 1. Gestão de Estoque
- 📦 Cadastrar produtos com código, nome, quantidade, unidade, preço unitário e validade.
- 📋 Listar produtos cadastrados no estoque.

### 👨‍🍳 2. Gestão da Cozinha
- 🍲 Adicionar pratos ao cardápio com nome, descrição, preço e ingredientes.
- 📜 Exibir o cardápio completo.

### 🍽️ 3. Gestão de Mesas e Pedidos
- 🪑 Cadastrar mesas com número, capacidade e status (ocupada/desocupada).
- 👀 Listar todas as mesas.
- 📝 Registrar pedidos por mesa com base no cardápio.
- 📦 Exibir os pedidos registrados.

### 💳 4. Pagamentos
- 💰 Calcular o valor total da conta por mesa.
- 💵 Escolher entre pagamento em dinheiro (com cálculo de troco) ou cartão (crédito/débito).
- ✅ Liberar mesa após o pagamento.

### 📈 5. Relatórios
- 🧾 Gerar um relatório de vendas com:
  - 🧮 Total por mesa
  - 🍝 Item mais vendido
  - 💸 Valor médio gasto por mesa

## 🧱 Estrutura Interna

O sistema utiliza quatro principais listas de dados:
- `estoque`: Lista de dicionários com informações dos produtos.
- `cardapio`: Lista de dicionários com os pratos disponíveis.
- `mesas`: Lista de mesas com status e pedidos vinculados.
- `pedidos`: Lista de pedidos registrados com total e itens.

