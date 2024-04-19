
# Projeto Coama - Cheat Sheet

Documento referente aos comandos e funções mais utilizadas durante o desenvolvimento do projeto.


## Apêndice

Aqui cobrimos os seguintes tópicos:

* Instalação dasdependências necessárias para executar o projeto;
* Comandos utilizados para executar o projeto;
* Localização de arquivos importantes para o front-end.


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`SECRET_KEY`

Para isso, entre em contato com [@PedroDanesvara](https://github.com/PedroDanesvara)



## Instalação do projeto

Primeiro verifique se o python está instalado com o seguinte comando:

```bash
  python --version
```

*Ps: A versão do python utilizada no projeto é a `3.10.10`*

Ele deve retornar a versão atual do seu python Ex.: `Python 3.10.10`

Instale todas as dependências necessárias com os seugintes comando:

```bash
  Python -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
```

Após isso você terá tudo o que é necessário para rodar o projeto.

É muito importante que você tenha a `SECRET_KEY` já configurada no seu .env

Para isso, entre em contato com [@PedroDanesvara](https://github.com/PedroDanesvara)
## Comandos Django

Iniciar servidor:

```bash
  python.exe .\manage.py runserver
```

Realizar atualização do banco de dados local:

```bash
  python.exe .\manage.py makemigrations
  python.exe .\manage.py migrate
```
## Localização dos arquivos front-end

O Django separa o projeto em *apps*. Cada *app* tem sua pasta. Nosso projeto atualmente conta com os apps:

```bash
  | - home
  | - login
```

Cada app tem sua própria pasta `templates` e `static`. A pasta `template` é responsável por armazenar todos os templates **HTML** que vão ser utilizados por cada app. A pasta `static` armazena os arquivos **css**, **js**, e **src** do projeto.

```bash
  | - home
  |   |-> static
  |             |-> css
  |             |-> js
  |             |-> src
  |   |-> templates
  | - login
  |       |-> static
  |             |-> css
  |             |-> js
  |             |-> src
  |       |-> templates
```
## Stack utilizada

**Front-end:** Html, Css, Js

**Back-end:** Django


## FAQ

#### Meus comandos não estão funcionando.

Tenha certeza que você está rodando o terminal no diretório raíz do projeto. Para confirmar isso digite o seguinte comando:

```bash
    ls -la
```

Esse comando vai listar todos os arquivos no diretório atual. Se a lista de arquivos conter todas as pastas que estão no repositório então você está rodando o terminal no diretório correto.


Qualquer dúvida entre em contato com [@PedroDanesvara](https://github.com/PedroDanesvara).


## Autores do README.md

- [@PedroDanesvara](https://github.com/PedroDanesvara)

