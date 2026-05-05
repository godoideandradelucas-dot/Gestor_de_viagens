# Projeto Gestor de Viagens - CRUD

## 📘 Descrição do Projeto

O objetivo principal é demonstrar como implementar operações **CRUD (Create, Read, Update, Delete)** em Python utilizando:

* funções (sem classes)
* dicionários e listas
* separação por ficheiros
* validação de dados

O projeto simula a gestão de um sistema de viagens com cinco entidades: **Viajante**, **Destino**, **Hotel**, **Voo** e **Viagem**.

---

## 🎯 Objetivos

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
     ├── voo.py
     ├── viagem.py
     └── utils.py
└── README.md
```

### main.py

Contém o **menu interativo em terminal**.

Responsável apenas por:

* apresentar as opções disponíveis
* recolher a escolha do utilizador
* chamar as funções dos módulos viajantes, destino, hotel, voo e viagem

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

### voo.py

Contém todas as operações CRUD da entidade **Voo**:

* `adicionar_voo()` — regista um novo voo
* `ver_voos()` — lista todos os voos
* `consultar_voo()` — pesquisa voo por ID
* `atualizar_voo()` — atualiza dados de um voo
* `remover_voo()` — remove um voo

Os voos são guardados numa **lista de dicionários em memória**.

---

### viagem.py

Contém todas as operações CRUD da entidade **Viagem**:

* `adicionar_viagem()` — regista uma nova viagem (associando voos, viajantes, hotel e destino)
* `ver_viagens()` — lista todas as viagens
* `consultar_viagem()` — pesquisa viagem por ID
* `atualizar_viagem()` — atualiza dados de uma viagem
* `remover_viagem()` — remove uma viagem

As viagens são guardadas numa **lista de dicionários em memória**.

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

**Validações de Voo:**
* `validar_companhia()` — apenas letras
* `validar_origem()` — apenas letras
* `validar_preco_voo()` — apenas números

**Validações de Viagem:**
* `validar_lista_nifs()` — lista de NIFs com 9 dígitos, separados por vírgula

**Validações de IDs:**
* `validar_id()` — número inteiro positivo
* `validar_id_destino()` — verifica se o ID existe na lista de destinos
* `validar_id_hotel()` — verifica se o ID existe na lista de hoteis
* `validar_id_voo()` — verifica se o ID existe na lista de voos
* `validar_id_voo_volta()` — permite indicar se existe voo de volta e valida o seu ID

**Funções de apresentação:**
* `mostrar_destinos_disponiveis()` — lista IDs e cidades dos destinos
* `mostrar_hoteis_disponiveis()` — lista IDs e nomes dos hoteis
* `mostrar_voos_disponiveis()` — lista IDs, companhias e origens dos voos
* `mostrar_viagens_disponiveis()` — lista IDs das viagens
* `mostrar_nifs_disponiveis()` — lista NIFs e nomes dos viajantes

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
id
pais
cidade
tipo
atracoes
```

### Hotel
```
id
nome
local
preco
tipo
```

### Voo
```
id
companhia
origem
id_destino
data_partida
data_chegada
preco
```

### Viagem
```
id
id_voo_ida
id_voo_volta
lista_id_viajantes
id_hotel
id_destino
```

---

## ▶️ Como Executar o Projeto

1️⃣ Garantir que Python está instalado

2️⃣ Executar no terminal:

```
python main.py
```

3️⃣ Utilizar o menu apresentado com as opções disponíveis

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
