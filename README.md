# Mapa da Jornada - Projeto e Desenvolvimento de Sistemas para Internet

O **Mapa da Jornada** é um software desenvolvido para a elucidação de conteúdos relacionados aos mais diversos âmbitos da Tecnologia da Informação, auxiliando usuários a visualizarem trilhas e competências necessárias para sua evolução profissional.

## 📋 Sobre o Projeto

Este sistema visa organizar o conhecimento técnico em TI, permitindo que usuários gerenciem seu aprendizado através de trilhas, projetos e visualização de competências.

### Funcionalidades
- **Autenticação:** Sistema completo de registro, login e logout.
- **Gerenciamento de Perfil:** Personalização e atualização de dados do usuário.
- **Gerenciamento de Projetos:** Organização de projetos pessoais.
- **Habilidades e Competências:** Cadastro e visualização de skills.
- **Áreas e Trilhas:** Visualização gráfica ou listada dos caminhos de aprendizado.
- **Painel Administrativo:** Gestão total do sistema via Django Admin.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Framework:** Django 5.2.7
- **Banco de Dados:** SQLite (padrão de desenvolvimento)
- **Processamento de Imagem:** Pillow 12.0.0
- **Outras bibliotecas:** `asgiref`, `sqlparse`, `tzdata`

---

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para rodar o projeto em seu ambiente local.

### Pré-requisitos
- Python 3.10 ou superior
- Virtualenv (recomendado)

### Passo a Passo

**1. Criar e ativar o ambiente virtual**
Recomendado para isolar as dependências do projeto.
```bash
python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

```


```bash
**2. Instalar dependências**

pip install -r requirements.txt

```

```bash
**3. Configurar o Banco de Dados Aplicar as migrações para criar as tabelas necessárias.**


python manage.py migrate
```

```bash
**4. Carregar Dados Iniciais Este passo é crucial para popular o sistema com as trilhas e configurações básicas.**

python manage.py loaddata mapa/fixtures/initial_data.json

```

```bash
**One-Liner**

python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; python manage.py migrate; python manage.py loaddata mapa/fixtures/initial_data.json; python manage.py runserver

```

### Árvore de Arquivos

MAPADAJORNADA/
├── config/                # Configurações do projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mapa/                  # App principal da aplicação
│   ├── fixtures/          # Dados iniciais (JSON)
│   ├── migrations/        # Histórico de banco de dados
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── outroshtmls/           # Arquivos HTML auxiliares
├── static/                # Arquivos estáticos (CSS, JS, Imagens)
├── templates/             # Templates HTML do Django
├── venv/                  # Ambiente Virtual
├── db.sqlite3             # Banco de dados
├── manage.py              # CLI do Django
├── README.md              # Documentação do projeto
└── requirements.txt       # Lista de dependências