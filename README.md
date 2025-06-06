# kdr-erp

## Peparando o ambiente

1. Clone o repositório

2. Acesse a pasta do projeto

3. Crie o ambiente virtual

    ```
    python -m venv venv
    ```

4. Acesse o ambiente virtual

    ```
    .\venv\Scripts\activate
    ```

5. Instale as bibliotecas

    ```
    pip install -r requirements.txt
    ```

6. Execute as migrations:

    ```
    python manage.py migrate
    ```

7. Execute o projeto:

    ```
    python manage.py runserver
    ```

## Instalando pacotes

Instale a biblioteca diretamente e crie o requirements.txt:

```
python -m pip install package
python -m pip freeze > requirements.txt
```

ou 

Adicione a biblioteca em requirements.txt e execute:

```
pip install -r requirements.txt
```

## Criando novo App

```
python manage.py startapp <app_name>
```

## Executando projeto como Desktop App

```
python gui.py
```

## Criando um batch file (.bat) para executar o projeto

```
@echo off
cmd /k "cd /d C:\<project_path>\venv\scripts & activate & cd /d C:\<project_path> & python gui.py & exit"
```

## Criando o executável do projeto

1. Crie o executável do projeto:

    ```
    pyinstaller --add-data "core;core" --add-data "kdr;kdr" --add-data "stock;stock" --add-data "manage.py;." --collect-all waitress --collect-all whitenoise gui.py
    ```

2. Adicione os arquivos .env e db.sqlite3 dentro da pasta:
    ```
    <project_path>\dist\<app_name>\_internal
    ```


**OBS 1: Caso exista o arquivo .spec, execute:**
```
pyinstaller gui.spec
```

**OBS 2: Opções adicionais para criar executável único:**
```
pyinstaller --onefile --windowed gui.spec
```