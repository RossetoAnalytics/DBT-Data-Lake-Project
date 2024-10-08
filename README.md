# DBT Data Lake Project

## Project Overview

Este projeto foi desenvolvido utilizando diversos recursos do DBT Core (Data Build Tool) e tem como objetivo demonstrar a criação de um Data Lake utilizando PostgreSQL hospedado no Amazon RDS. O projeto inclui a utilização do DBeaver como sistema de gerenciamento de banco de dados local.

### Recursos Utilizados
- **DBT-Core**: Ferramenta de transformação de dados que permite a modelagem, documentação e testes de dados de forma eficiente.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar os dados.
- **Amazon RDS**: Serviço gerenciado de banco de dados da AWS que fornece um ambiente escalável e seguro para o PostgreSQL.
- **DBeaver**: Ferramenta de gerenciamento de banco de dados que permite a conexão e manipulação dos dados localmente.
- **Faker**: Biblioteca utilizada para gerar dados fictícios e populá-los nas tabelas.

### Arquitetura
O projeto foi estruturado seguindo a arquitetura de Data Lake, que inclui os seguintes componentes:

- **Models**: Modelos que definem a estrutura e as transformações dos dados.
- **Macros**: Funções reutilizáveis que ajudam na simplificação de transformações complexas.
- **Seeds**: Tabelas que contêm dados estáticos, utilizados como base para outras transformações.
- **Snapshots**: Mecanismo para capturar o estado dos dados em intervalos de tempo específicos, permitindo o rastreamento de mudanças.

## Getting Started

### Pré-requisitos

- **Python**: Certifique-se de ter o Python instalado em sua máquina.
- **DBT**: Instale o DBT em sua máquina. Você pode encontrar instruções de instalação [aqui](https://docs.getdbt.com/docs/installation).
- **PostgreSQL**: Ter acesso a um banco de dados PostgreSQL (local ou na nuvem).

### Instalação

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd <NOME_DO_DIRETÓRIO>
