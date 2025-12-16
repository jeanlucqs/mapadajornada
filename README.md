# Mapa da Jornada - Projeto e Desenvolvimento de Sistemas para Internet

Este README fornece instruções mínimas para rodar o projeto.

## Requisitos

- Python 3.10 ou superior
- Virtualenv (opcional, mas recomendado)

## Passo a passo para executar o projeto

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Aplicar migrações
python manage.py migrate

# 4. Carregar dados iniciais
python manage.py loaddata mapa/fixtures/initial_data.json

# 5. Rodar o servidor
python manage.py runserver

# 6. Opcional (Caso queira rodar através de uma linha de comando):
python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; python manage.py migrate; python manage.py loaddata mapa/fixtures/initial_data.json; python manage.py runserver