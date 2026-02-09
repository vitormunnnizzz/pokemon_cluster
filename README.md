# 🐱‍👤 Pokémon Data Analysis & Clustering

Este projeto realiza a **coleta, análise e clusterização de dados de Pokémon**, utilizando dados públicos da **PokeAPI**.
O objetivo é explorar características dos Pokémon e aplicar técnicas de **análise exploratória e aprendizado não supervisionado** para identificar padrões entre eles.

---

## 📌 Funcionalidades

* 📡 Coleta automática de dados da **PokeAPI**
* 🚀 API desenvolvida com **FastAPI**
* 📊 Análise exploratória de dados (EDA)
* 🤖 Clusterização de Pokémon com **Machine Learning**
* 📈 Visualização e interpretação dos clusters

---

## 🗂 Estrutura do Projeto

```bash
├── main.py                  # API FastAPI para coleta dos dados
├── cluster_pokemon.ipynb    # Notebook com EDA e clusterização
├── README.md                # Documentação do projeto
└── requirements.txt         # Dependências do projeto
```

---

## 🛠 Tecnologias Utilizadas

* **Python**
* **FastAPI**
* **Requests**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib / Seaborn**
* **Jupyter Notebook**

---

## 📥 Coleta de Dados

Os dados são obtidos via **PokeAPI**, incluindo informações como:

* Nome do Pokémon
* Altura e peso
* Tipo principal
* Status base (HP, ataque, defesa, etc.)
* Quantidade de habilidades
* Quantidade de movimentos

A API disponibiliza esses dados no endpoint:

```http
GET /dataset-pokemon
```

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a API

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Análise e Clusterização

No notebook `cluster_pokemon.ipynb` são realizadas:

* Limpeza e preparação dos dados
* Análise exploratória (EDA)
* Padronização das variáveis
* Aplicação de algoritmos de clusterização (ex: K-Means)
* Visualização e interpretação dos grupos formados

---

## 🎯 Objetivo do Projeto

Este projeto tem fins **educacionais e exploratórios**, sendo ideal para:

* Portfólio de **Data Science / Machine Learning**
* Estudos de **aprendizado não supervisionado**
* Demonstração de integração entre **API + análise de dados**

---

## 📄 Fonte dos Dados

* [PokeAPI](https://pokeapi.co/)

---

## 👤 Autor

**Vitor Hugo Muniz**
Engenharia da Computação | Ciência de Dados
📍 UFC – Universidade Federal do Ceará
