# Testes Automatizados com Pytest e Pytest-cov

## Requisitos
* Python >= 3.8

### Configuração do Ambiente

1. Criar ambiente virtual
    ```sh
    $ python -m venv .venv
    ```
2. Ativar o ambiente virtual
    ```sh
    $ source .venv\bin\activate # GNU/Linux
    $ \.venv\bin\activate.ps1 # Windows (Power Shell)
    ```
3. Instalar as dependências
    ```sh
    $ pip install -r requirementes.txt
    ```
4. Executar testes
    ```sh
    $ pytest
    ```
5. Gerar relatório HTML e XML
    ```sh
    $ pytest --cov-report html --cov-report=xml:coverage_reports/coverage.xml
    ```
