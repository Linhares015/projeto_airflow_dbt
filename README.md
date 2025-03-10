# Projeto: Orquestração do DBT no Airflow Astro

Este projeto demonstra como orquestrar o DBT (Data Build Tool) utilizando o Airflow Astro. Nosso foco inicial é a configuração do ambiente com o Astro CLI no Windows Subsystem for Linux (WSL) e a instalação do Docker. Os exemplos de DAG já estão presentes no repositório. No final, detalhamos a integração com o Cosmos DBT.

---

---
## Aulas YouTube

 - [Vídeo 1 - Conceitos](https://youtu.be/k-XcMH4P_34)
 - [Vídeo 2 - Configurando Ambiente, Criando primeira DAG]()

---
## Sumário

- [Requisitos](#requisitos)
- [Instalação e Configuração do Ambiente](#instalação-e-configuração-do-ambiente)
  - [1. Configuração do WSL](#1-configuração-do-wsl)
  - [2. Instalação do Docker](#2-instalação-do-docker)
  - [3. Instalação do Astro CLI](#3-instalação-do-astro-cli)
- [Deploy do Projeto](#deploy-do-projeto)
- [Integração com Cosmos DBT](#integração-com-cosmos-dbt)
- [Recursos Adicionais](#recursos-adicionais)

---

## Requisitos

- **WSL (Windows Subsystem for Linux):** Para uma experiência Linux nativa no Windows.
- **Docker:** Necessário para executar os containers do Airflow e outros serviços.
- **Astro CLI:** Ferramenta de linha de comando para gerenciar e deployar ambientes Airflow Astro.
- **Projeto DBT:** Já incluído ou montado via volume conforme as necessidades do ambiente.

---

## Instalação e Configuração do Ambiente

### 1. Configuração do WSL

Certifique-se de que o WSL está instalado e configurado no seu sistema Windows. Recomendamos utilizar o **WSL 2** para melhor performance. Caso ainda não tenha, siga os passos abaixo:

1. Habilite o WSL:
   - Abra o PowerShell como Administrador e execute:
     ```
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     ```
2. Habilite a Plataforma de Máquina Virtual:
   - No mesmo terminal, execute:
     ```
     dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
     ```
3. Reinicie o computador.
4. Instale uma distribuição Linux (por exemplo, Ubuntu) pela Microsoft Store.
5. Atualize o WSL para a versão 2 (se necessário):
   ```
   wsl --set-version Ubuntu 2
   ```

### 2. Instalação do Docker

O Docker é essencial para executar o Airflow em containers. Siga estas instruções:

1. Instale o **Docker Desktop para Windows**:
   - Faça o download em [docker.com](https://www.docker.com/products/docker-desktop) e siga o assistente de instalação.
2. Certifique-se de que o Docker está configurado para usar o WSL 2:
   - No Docker Desktop, acesse as configurações e habilite a integração com sua distribuição Linux instalada (por exemplo, Ubuntu).

Verifique a instalação executando no terminal do WSL:
```
docker --version
```

### 3. Instalação do Astro CLI

O Astro CLI é a ferramenta oficial para gerenciar ambientes Airflow Astro. Para instalá-lo no WSL, siga os passos:

1. Abra o terminal do WSL.
2. Execute o script de instalação:
   ```
   curl -sSL https://install.astronomer.io | sudo bash
   ```
   *Obs.: Verifique a [documentação oficial do Astronomer](https://docs.astronomer.io/) para possíveis atualizações no método de instalação.*

3. Após a instalação, verifique se o Astro CLI está instalado:
   ```
   astro version
   ```

---

## Deploy do Projeto

1. **Clone o Repositório:**
   Clone este repositório para o seu ambiente WSL.

   ```
   git clone <URL-do-repositório>
   cd <nome-do-repositório>
   ```

2. **Configuração dos Arquivos DBT:**
   Certifique-se de que o seu projeto DBT (incluindo o arquivo `profiles.yml`) esteja disponível:
   - **Inclusão na Imagem:** Caso os arquivos estejam “bakeados” na imagem.
   - **Montagem via Volume:** Configure o Docker Compose para montar o diretório do projeto DBT no container do Airflow.

3. **Deploy com Astro CLI:**
   Utilize o Astro CLI para fazer o deploy do seu ambiente Airflow Astro.

   ```
   astro dev init
   astro dev start
   ```

   Esses comandos irão inicializar e iniciar seu ambiente local do Airflow Astro, que pode ser acessado via [http://localhost:8080](http://localhost:8080).

4. **Verificação:**
   Acesse a interface web do Airflow e verifique se as DAGs do projeto estão listadas (os exemplos de DAG já estão incluídos no repositório).

---

## Integração com Cosmos DBT

A integração do DBT com o Airflow utilizando o operador Cosmos DBT é abordada nesta configuração para orquestrar comandos DBT de forma simplificada.
**Observação:** Detalhes e parâmetros específicos da integração com o Cosmos DBT estão descritos na seção final da documentação deste projeto. Consulte essa seção para ajustar o operador conforme seu ambiente.

---

## Recursos Adicionais

- [Documentação do Astronomer](https://docs.astronomer.io/)
- [Documentação do Astro CLI](https://docs.astronomer.io/)
- [DBT Documentation](https://docs.getdbt.com/)
- [Airflow Documentation](https://airflow.apache.org/docs/)
