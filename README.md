# Apollo

## O que é o Apollo

O Apollo é uma plataforma SaaS onde alunos enviam suas respostas de provas do ENEM (edições de 2019 em diante) e recebem uma análise criteriosa dos erros cometidos. A partir dessas respostas, o sistema identifica as áreas de conhecimento e habilidades em que o aluno mais precisa melhorar e calcula a nota estimada por área usando a Teoria de Resposta ao Item (TRI) — a mesma metodologia usada pelo INEP para apurar a nota oficial do ENEM.

A ideia central é resolver um problema comum: a maioria das ferramentas de simulado entrega apenas "acertou/errou" e uma nota final, sem indicar em que competências o aluno realmente precisa focar. O Apollo decompõe esse resultado em um dashboard por área de conhecimento, permitindo que o aluno estude de forma direcionada em vez de repetir simulados às cegas.

O projeto está sendo desenvolvido como parte da disciplina de Cloud, com toda a arquitetura documentada em RUP/UP (Documento de Visão, Requisitos Suplementares, Casos de Uso Arquiteturais e Modelo de Análise) e implantação em nuvem na AWS.

## Este repositório: recorte reduzido para deploy em Elastic Beanstalk

Este repositório específico **não é o Apollo completo** — é um recorte reduzido, feito para um exercício de outra disciplina (também do mesmo professor) cujo objetivo é demonstrar deploy em **AWS Elastic Beanstalk**.

A arquitetura completa do Apollo prevê múltiplas entidades (provas, questões, respostas por item, parâmetros de TRI, sessões de correção, etc.) e uma stack AWS mais ampla — EC2, RDS, DynamoDB, S3, API Gateway, Lambda, Secrets Manager e CloudWatch (ver o Documento de Visão e o Modelo de Análise do projeto principal). Para este exercício de Elastic Beanstalk, o escopo foi deliberadamente reduzido a **duas classes**, suficientes para demonstrar o fluxo de deploy sem replicar a arquitetura completa:

- **`Aluno`** — estudante cadastrado na plataforma (nome, e-mail).
- **`Avaliacao`** — uma avaliação/simulado do ENEM feito por um aluno (ano, área de conhecimento, nota TRI), associada a um `Aluno` (relação 1:N).

Não há aqui: cálculo real de TRI, múltiplas questões por avaliação, autenticação de usuário ou os demais serviços AWS do projeto maior. O banco usado é SQLite (não RDS), por simplicidade de deploy nesta etapa.

## Estrutura do projeto

```
apollo_eb/
├── apollo/                 # configuração do projeto Django (settings, urls, wsgi)
├── avaliacoes/              # app com as classes Aluno e Avaliacao
│   ├── models.py             # definição das 2 classes
│   ├── serializers.py        # serializers DRF (com avaliações aninhadas no aluno)
│   ├── views.py               # ModelViewSets (CRUD via API REST)
│   ├── urls.py
│   └── admin.py
├── .ebextensions/            # configuração de deploy do Elastic Beanstalk
├── Procfile
├── requirements.txt
└── manage.py
```

## Modelo de dados (deste recorte)

```
Aluno (1) ──< Avaliacao (N)
```

| Campo (Aluno) | Tipo |
|---|---|
| nome | CharField |
| email | EmailField (único) |

| Campo (Avaliacao) | Tipo |
|---|---|
| aluno | ForeignKey → Aluno |
| ano | IntegerField (edição do ENEM, ex.: 2025) |
| area | CharField (LC, CH, CN, MT) |
| nota_tri | DecimalField |
| data_criacao | DateTimeField (auto) |

## Stack

- Python / Django 6.0 + Django REST Framework
- SQLite (banco local, sem RDS nesta etapa)
- Gunicorn (servidor WSGI)
- AWS Elastic Beanstalk (plataforma de deploy)

## Rodando localmente

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

A API fica disponível em `/api/alunos/` e `/api/avaliacoes/` (ModelViewSets padrão do DRF).

## Deploy no Elastic Beanstalk

O projeto já inclui `.ebextensions/` e `.elasticbeanstalk/config.yml` configurados para o deploy via `eb deploy`, seguindo o template fornecido pelo professor para a disciplina.

## Próximos passos (fora do escopo atual)

- Adaptar o modelo para incluir autenticação/login de aluno.
- Reintegrar com a arquitetura completa do Apollo (RDS, DynamoDB, API Gateway + Lambda para ingestão) quando o exercício de Elastic Beanstalk evoluir para o projeto principal.
