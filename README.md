# DBT Data Lake Project

## Project Overview

Este projeto foi desenvolvido utilizando vários recursos do **DBT-Core** e configurações do **PostgreSQL** em um **RDS da AWS**. O **DBeaver** foi utilizado como sistema de gerenciamento local. O projeto gera tabelas usando a biblioteca **Faker**, seguindo uma arquitetura de **Data Lake**. 


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

### Pré-requisitos

- **Python**: Certifique-se de ter o Python instalado em sua máquina.
- **DBT**: Instale o DBT em sua máquina. Você pode encontrar instruções de instalação [aqui](https://docs.getdbt.com/docs/installation).
- **PostgreSQL**: Ter acesso a um banco de dados PostgreSQL (local ou na nuvem).

### Resultados

<details>
  <summary>Visuais</summary>

**Lineage no DBT Localhost**
![dbt-marts-run-lineage](https://github.com/user-attachments/assets/c1ad890c-8a2f-40cb-a016-a9ba6863e591)

**Estrutura no Dbeaver**
![dbt-mart](https://github.com/user-attachments/assets/7ceac08c-47d0-4267-be88-43b055b717e2)

</details>

### Documentação

<details>
  <summary>Visuais</summary>

![dbt-mart-localhost](https://github.com/user-attachments/assets/86d1dadf-1a7a-49b7-a640-ab03cecd16cb)


</details>

A documentação do projeto foi gerada e pode ser visualizada em um ambiente local. Os seguintes comandos foram utilizados:

```bash
dbt docs generate
dbt serve
