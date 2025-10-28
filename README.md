# Carteiro um bot de Notícias para Discord

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.3-7289DA.svg)](https://discordpy.readthedocs.io/en/latest/)
[![AWS](https://img.shields.io/badge/Deploy-AWS%20EC2-FF9900.svg)](https://aws.amazon.com/ec2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um bot para Discord autônomo e proativo, construído com **Python** e `discord.py`, que mantém um servidor atualizado com as últimas notícias. O bot busca manchetes de portais de notícias através de feeds **RSS** e as entrega em canais específicos de forma automática e sob demanda.

O projeto foi totalmente implantado na **AWS (Amazon Web Services)**, rodando como um serviço persistente em uma instância EC2 para garantir operação 24/7.

## ✨ Demonstração em Ação

<img width="302" height="210" alt="image" src="https://github.com/user-attachments/assets/a42dbedf-3157-49d2-8937-228dfa16d508" />
<img width="663" height="428" alt="image" src="https://github.com/user-attachments/assets/e7a866a4-2e5b-4d60-aa49-1ff3d0278626" />


## 🏛️ Arquitetura e Funcionalidades

Este bot foi projetado para ser um serviço robusto e eficiente, combinando programação orientada a eventos com tarefas agendadas.

### Funcionalidades Principais
-   **Entrega Automática de Notícias:** Utilizando a extensão `tasks` do `discord.py`, o bot busca e envia as 10 principais notícias para um canal pré-configurado a cada 3 horas, mantendo a comunidade informada de forma autônoma.
-   **Busca de Notícias sob Demanda:** Responde ao comando `!noticias` para buscar e exibir instantaneamente as 10 últimas manchetes.
-   **Parsing de Feeds RSS:** Utiliza a biblioteca `feedparser` para consumir feeds RSS de portais de notícias, uma abordagem robusta que não depende de chaves de API.
-   **Limpeza de HTML:** Emprega o `BeautifulSoup` para analisar e limpar o conteúdo HTML dos resumos das notícias, garantindo que as mensagens no Discord sejam limpas, legíveis e sem tags indesejadas.
-   **Formatação Profissional com Embeds:** As notícias são apresentadas em "Embeds" do Discord, com títulos clicáveis, resumos concisos e uma formatação visualmente agradável.

## ☁️ Implantação (Deploy) na AWS

Para garantir a operação contínua (24/7), o bot foi implantado em uma instância **EC2 t2.micro** na **AWS**, dentro do Free Tier.

-   O ambiente no servidor foi configurado em uma máquina **Ubuntu Linux**.
-   A aplicação roda como um serviço persistente gerenciado pelo **`systemd`**, garantindo que o bot seja reiniciado automaticamente em caso de falha ou após um reboot do servidor.
-   A segurança é garantida por um **Security Group** que limita o acesso SSH apenas a IPs autorizados.

## 🛠️ Stack Tecnológico

| Área | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Core** | Python 3.10+ | Linguagem principal |
| | discord.py | Interação com a API do Discord e tarefas agendadas |
| | feedparser | Análise de feeds RSS/XML |
| | BeautifulSoup4 | Limpeza de HTML dos resumos das notícias |
| | python-dotenv | Gerenciamento de segredos (token do bot) |
| **Deploy** | AWS EC2 | Hospedagem em servidor virtual na nuvem |
| | Ubuntu Linux | Sistema operacional do servidor |
| | systemd | Gerenciamento do processo como um serviço persistente |
| | SSH | Acesso seguro e gerenciamento do servidor |

## ⚙️ Como Executar o Projeto Localmente

### 1. Pré-requisitos
-   Python 3.10 ou superior.
-   Uma conta no Discord e um servidor para testes.
-   Ter criado uma Aplicação de Bot no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications) e ter o **token** do bot.

### 2. Configuração do Ambiente
```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/discord-news-bot.git](https://github.com/seu-usuario/discord-news-bot.git)
cd discord-news-bot

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configure seus Segredos
-   Crie um arquivo chamado `.env` na raiz do projeto.
-   Adicione suas credenciais a ele:
    ```
    DISCORD_TOKEN=seu_token_secreto_aqui
    NEWS_CHANNEL_ID=id_do_canal_de_noticias_aqui
    ```

### 4. Iniciar o Bot
```bash
# Com a venv ativa, execute o script
python3 bot.py
```
✅ O bot ficará online no seu servidor do Discord e responderá aos comandos.
