
# Projeto Coama - Cheat Sheet

Documento referente aos comandos e funções mais utilizadas durante o desenvolvimento do projeto.


## Apêndice

Aqui cobrimos os seguintes tópicos:

* Instalação dasdependências necessárias para executar o projeto;
* Comandos utilizados para executar o projeto;
* Localização de arquivos importantes para o front-end.
* Comandos git importantes


## Stack utilizada

**Front-end:** Html, Css, Js

**Back-end:** Django


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
## Comandos git

Antes de começar tudo, verifique se está na branch correta. Caso contrário crie sua branch no GitHub ou com os seguintes comandos:

```bash
  git branch <branch_name>
  git push <remote_name> <branch_name>
```

#### Enviar commit das mudanças realizadas:

```bash
  git add .
  git commit -m "<your_commit_message>"
  git push
```

#### Padrão de nomeclatura nos commits:

```bash
  <type>: <description>
```

types:

**`feat`** : a new feature is introduced with the changes;

**`fix`** : a bug fix has occurred;

**`chore`** : changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies);

**`refactor`** : refactored code that neither fixes a bug nor adds a feature;

**`docs`** : updates to documentation such as a the README or other markdown files;

**`style`** : changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on;

**`test`** : including new or correcting previous tests;

**`perf`** : performance improvements;

**`ci`** :  continuous integration related;

**`build`** : changes that affect the build system or external dependencies;

**`revert`** : reverts a previous commit.

- **Referência:** [Freecodecamp.org](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/#conventional-commits)

---

#### Alterar sua branch atual no seu ambiente de desenvolvimento:

```bash
  git checkout <branch-name>
```




Qualquer dúvida entre em contato com [@PedroDanesvara](https://github.com/PedroDanesvara).
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
