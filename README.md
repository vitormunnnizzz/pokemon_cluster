# Descrição

Este projeto realiza a **coleta, análise e clusterização de dados de Pokémon**, utilizando dados públicos da **[PokeAPI](https://pokeapi.co/)**. O objetivo é explorar características dos Pokémon e aplicar técnicas de **análise exploratória e aprendizado não supervisionado** para identificar padrões entre eles.

## Funcionalidades

* Coleta automática de dados da **PokeAPI**
* API desenvolvida com **FastAPI**
* Análise exploratória de dados (EDA)
* Clusterização de Pokémon com **Machine Learning**
* Visualização e interpretação dos clusters


## Estrutura do Projeto

```bash
├── main.py                  # API FastAPI para coleta dos dados
├── cluster_pokemon.ipynb    # Notebook com EDA e clusterização
├── README.md                # Documentação do projeto
└── requirements.txt         # Dependências do projeto
```

## Tecnologias Utilizadas

* **Python**
* **FastAPI**
* **Requests**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib / Seaborn**
* **Jupyter Notebook**

## Coleta de Dados

Os dados são obtidos via **PokeAPI**, incluindo informações como:

* Nome do Pokémon
* Altura e peso
* Tipo principal
* Status base (HP, ataque, defesa, etc.)
* Quantidade de habilidades
* Quantidade de movimentos

## Como Executar o Projeto

### 1️Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️Criar ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️Executar a API

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

## Análise e Clusterização

No notebook `cluster_pokemon.ipynb` são realizadas:

* Limpeza e preparação dos dados
* Análise exploratória (EDA)
* Padronização das variáveis
* Aplicação de algoritmos de clusterização (ex: K-Means)
* Visualização e interpretação dos grupos formados

## Autor

**Vitor Hugo Muniz de Sousa Santos**

Engenheiro da Computação | Especialista em Ciência de Dados

*  [vitormunnnizzz@gmail.com](mailto:vitormunnnizzz@gmail.com)
*  [www.linkedin.com/in/vitormunnnizzz](https://www.linkedin.com/in/vitormunnnizzz)
