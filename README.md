# Projeto Gestor de Viagens - CRUD

## 📘 Descrição do Projeto

O objetivo principal é demonstrar como implementar operações **CRUD (Create, Read, Update, Delete)** em Python utilizando:

* funções (sem classes)
* dicionários e listas
* separação por ficheiros
* validação de dados

O projeto simula a gestão de um sistema de viagens com três entidades: **Viajante**, **Destino** e **Hotel**.

---

## 🎯 Objetivos Pedagógicos

Com este projeto devemos aprender a:

* organizar código em múltiplos ficheiros Python
* utilizar dicionários como estrutura de armazenamento
* implementar operações CRUD
* validar dados introduzidos pelo utilizador
* separar lógica de negócio da interface (menu)
* importar funções entre ficheiros

---

## 📂 Estrutura do Projeto

```
.
└── Gestor_viagens
     ├── main.py
     ├── viajantes.py
     ├── destino.py
     ├── hotel.py
     └── utils.py
└── README.md
```

### main.py

Contém o **menu interativo em terminal**.

Responsável apenas por:

* apresentar as 15 opções disponíveis
* recolher a escolha do utilizador
* chamar as funções dos módulos viajantes, destino e hotel

---

### viajantes.py

Contém todas as operações CRUD da entidade **Viajante**:

* `adicionar_viajante()` — regista um novo viajante
* `ver_viajantes()` — lista todos os viajantes
* `consultar_viajantes()` — pesquisa viajante por nome
* `atualizar_viajantes()` — atualiza dados de um viajante
* `remover_viajantes()` — remove um viajante

Os viajantes são guardados numa **lista de dicionários em memória**.

---

### destino.py

Contém todas as operações CRUD da entidade **Destino**:

* `adicionar_destino()` — regista um novo destino
* `ver_destinos()` — lista todos os destinos
* `consultar_destinos()` — pesquisa destino por país
* `atualizar_destino()` — atualiza dados de um destino
* `remover_destino()` — remove um destino

Os destinos são guardados numa **lista de dicionários em memória**.

---

### hotel.py

Contém todas as operações CRUD da entidade **Hotel**:

* `adicionar_hotel()` — regista um novo hotel
* `ver_hoteis()` — lista todos os hoteis
* `consultar_hotel()` — pesquisa hotel por nome
* `atualizar_hotel()` — atualiza dados de um hotel
* `remover_hotel()` — remove um hotel

Os hoteis são guardados numa **lista de dicionários em memória**.

---

### utils.py

Contém todas as funções auxiliares partilhadas pelos módulos:

**Verificações de listas:**
* `verificar_viajantes(viajantes)` — verifica se há viajantes registados
* `verificar_destinos(destinos)` — verifica se há destinos registados
* `verificar_hoteis(hoteis)` — verifica se há hoteis registados

**Validações de Viajante:**
* `validar_nome()` — apenas letras
* `validar_data()` — formato DD/MM/AAAA usando `datetime`
* `validar_nacionalidade()` — apenas letras
* `validar_telefone()` — 9 dígitos numéricos
* `validar_email()` — deve conter @gmail.com
* `validar_NIF()` — 9 dígitos numéricos
* `validar_interesses()` — apenas letras
* `validar_orcamento()` — apenas números

**Validações de Destino:**
* `validar_pais()` — apenas letras
* `validar_cidade()` — apenas letras
* `validar_tipo()` — apenas letras (praia, urbano, montanha, natureza)
* `validar_atracoes()` — apenas letras

**Validações de Hotel:**
* `validar_hotel()` — apenas letras
* `validar_local()` — apenas letras
* `validar_preco()` — apenas números
* `validar_tipo_hotel()` — apenas letras (hotel, pousada, resort)

---

## 👤 Estrutura das Entidades

### Viajante
```
nome
data_nascimento
nacionalidade
telefone
email
NIF
interesses
orcamento
```

### Destino
```
pais
cidade
tipo
atracoes
```

### Hotel
```
nome
local
preco
tipo
```

---

## ▶️ Como Executar o Projeto

1️⃣ Garantir que Python está instalado

2️⃣ Executar no terminal:

```
python main.py
```

3️⃣ Utilizar o menu apresentado com as opções de 0 a 15

---

## 📋 Menu do Sistema

```
----------------------------- Gestor de Viagens -----------------------------
1 - Adicionar viajante     6 - Adicionar destino     11 - Adicionar hotel
2 - Ver viajantes          7 - Ver destinos          12 - Ver hoteis
3 - Consultar viajante     8 - Consultar destino     13 - Consultar hotel
4 - Atualizar viajante     9 - Atualizar destino     14 - Atualizar hotel
5 - Remover viajante       10 - Remover destino      15 - Remover hotel

                                0 - sair
----------------------------------------------------------------------------
```

---

## 📚 Conceitos Trabalhados

Este projeto permite consolidar:

* funções
* dicionários e listas
* módulos Python
* importação entre ficheiros
* validação de dados com `while`
* estruturas condicionais (`if/elif/else`)
* ciclos (`while`, `for`)

---

## 👨‍🏫 Utilização em Sala de Aula

Este projeto vai ser usado para:

* introdução ao CRUD
* exercícios guiados
* avaliação prática
* preparação para projetos maiores
