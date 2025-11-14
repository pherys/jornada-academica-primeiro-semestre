# 🌿 Projeto: O Jardim Digital (Lógica e API)

Bem-vindo ao Jardim Digital\! Este repositório contém dois exemplos de código em Python criados para demonstrar conceitos de programação, desde uma lógica condicional simples até uma API web funcional com cliente.

## 🗂️ O que você encontrará aqui?

Este projeto é dividido em duas partes principais:

1.  **Parte 1: A Lógica da Planta (`jardim_logica_aula1.py`)**

      * Um script Python simples e independente que simula a lógica de cuidar de uma planta.
      * Perfeito para entender como funcionam as declarações `if/else` (SE/SENÃO).

2.  **Parte 2: A API do Jardim (Cliente-Servidor)**

      * Uma mini aplicação web que demonstra como um "cliente" (página web) conversa com um "servidor" (API).
      * **Arquivos:**
          * `servidor.py`: O "Jardineiro" (nossa API em Flask) que espera por chamadas.
          * `index.html`: O "Visitante" (nosso site) que "aperta a campainha" (botão) para chamar o servidor.

-----

## 🚀 Parte 1: Testando a Lógica da Planta (Standalone)

Este script (`jardim_logica_aula1.py`) não precisa de instalação. Você pode rodá-lo diretamente para ver a lógica `if/else` em ação.

### Como Rodar:

1.  Abra seu terminal (Prompt de Comando, PowerShell, etc.).

2.  Navegue até a pasta onde você salvou os arquivos.

3.  Execute o seguinte comando:

    ```bash
    python jardim_logica_aula1.py
    ```

4.  Você verá o resultado no terminal, mostrando as etapas de cuidado com base na condição da terra.

### 💡 Experimente\!

Abra o arquivo `jardim_logica_aula1.py` em um editor de texto e mude o valor da variável `terra_esta_seca` (linha 11) de `True` para `False`. Salve o arquivo e rode o script novamente para ver como o resultado da lógica muda\!

-----

## 🚀 Parte 2: Testando a API do Jardim (Cliente-Servidor)

Aqui, vamos fazer o "Visitante" (`index.html`) conversar com o "Jardineiro" (`servidor.py`). Isso requer uma pequena configuração inicial para instalar as "ferramentas" do servidor.

### 🔧 1. Configuração do Ambiente (Feito apenas uma vez)

Para que o `servidor.py` funcione, ele precisa das bibliotecas `Flask` e `Flask-Cors`. Vamos instalá-las de forma organizada usando um **Ambiente Virtual** (`venv`).

#### O que é um `venv` (Ambiente Virtual)?

Pense no `venv` como uma "caixa de ferramentas" isolada e dedicada apenas para este projeto. Em vez de instalar o Flask "solto" no seu computador (o que pode causar conflitos com outros projetos), nós o instalamos dentro desta caixa.

O arquivo `.gitignore` está configurado para **ignorar** a pasta `venv/`. Isso é uma boa prática porque nunca enviamos a "caixa de ferramentas" inteira para o repositório (ela pode ser muito grande e específica do sistema). Enviamos apenas a *lista* do que é necessário (neste caso, `Flask` e `Flask-Cors`), e cada pessoa que baixa o projeto cria sua própria caixa local.

#### Passos para Configurar:

1.  **Abra o terminal** na pasta do projeto.

2.  **Crie o ambiente virtual** (a "caixa"):

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente** (abra a "caixa"):

      * **No Windows (PowerShell/CMD):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **No macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
      * (Você saberá que funcionou, pois o nome `(venv)` aparecerá no início da linha do seu terminal).

4.  **Instale as ferramentas** (Flask e Flask-Cors) dentro da caixa:

    ```bash
    pip install Flask Flask-Cors
    ```

Pronto\! Seu ambiente está configurado.

### 🖥️ 2. Como Rodar a Aplicação

Você precisará de **duas coisas abertas**: (1) o terminal rodando o servidor e (2) o seu navegador com o `index.html`.

#### Passo A: Iniciar o Servidor (O Jardineiro)

1.  Certifique-se de que seu ambiente virtual `(venv)` está **ativo** no terminal (veja o passo de ativação acima).
2.  No terminal, execute o servidor Python:
    ```bash
    python servidor.py
    ```
3.  O terminal mostrará que o servidor está rodando, algo como: `Running on http://127.0.0.1:5000/`.
4.  **Deixe este terminal aberto\!** Se você fechá-lo, o "Jardineiro" (servidor) vai "dormir" e não poderá atender o "Visitante".

#### Passo B: Abrir o Cliente (O Visitante)

1.  Vá até a pasta do projeto no seu computador.
2.  Encontre o arquivo `index.html`.
3.  **Abra-o diretamente no seu navegador** (clique duas vezes sobre ele, ou "Abrir com" \> "Google Chrome/Firefox/etc.").

#### Passo C: Testar a Comunicação

1.  Com a página `index.html` ("O Visitante do Jardim") aberta no navegador.
2.  Clique no botão verde: **"Apertar a Campainha (Chamar API)"**.
3.  Observe a "Resposta do Jardineiro (Servidor)":
      * Ela mudará de "Aguardando..." para **"Nosso Jardim (API) está funcionando\!"**.

Isso confirma que o `index.html` (frontend) conseguiu chamar o `servidor.py` (backend) e receber uma resposta com sucesso\!

### 🚨 Solução de Problemas

  * **Se o status mostrar "ERRO\! Não consegui falar com o Jardineiro..."**:
      * Verifique se o terminal do **Passo A** (`python servidor.py`) ainda está aberto e rodando.
      * Verifique se você instalou o `Flask` e o `Flask-Cors` (Passo de Configuração).
      * Verifique se o seu firewall não está bloqueando a porta `5000`.
