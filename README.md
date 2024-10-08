<img width="120" height="120" align="right" alt="logo ClientConnect" src="https://github.com/user-attachments/assets/b3f7d1b0-0e0b-4cb9-b7c4-7c9abc1e3d65">
<a href="https://smbot.com.br/" target="_blank">
  <img width="120" height="120" align="right" alt="logo SMBOT" src="https://github.com/user-attachments/assets/0893b658-341e-4d28-91a5-b994cb06ecf2">
</a>

# ClientConnect

Este projeto foi desenvolvido como parte do Desafio Técnico para a vaga de Desenvolvedor Backend no Grupo SM.

[![Descrição do Desafio](https://img.shields.io/badge/Descrição_do_Desafio-Informational?style=for-the-badge&logo=google-docs&logoColor=white&color=3955FF)](https://docs.google.com/document/d/1vb9WExZmk7XXVcp_gMAZ3EK4p8JePjgHS335UGe4vAc/edit?usp=sharing)
[![Documentação API](https://img.shields.io/badge/Documentação_API-Informational?style=for-the-badge&logo=postman&logoColor=white&color=D400CF)](https://documenter.getpostman.com/view/29600204/2sAXqng58h)
[![Figma](https://img.shields.io/badge/Figma-Informational?style=for-the-badge&logo=figma&logoColor=white&color=9400D4)](https://www.figma.com/board/4j8PhXe6WIa10wKMLwXPOt/Desafio-SMBOT---Matheus-Banqueiro-Lima?node-id=0-1&t=OXnSNABngLUJKwap-1)


## Tecnologias Principais

<img src="https://github.com/user-attachments/assets/d26f4f95-e67b-443d-8f65-68380ba211f5" width="30" height="30" alt="Django">
<img src="https://github.com/user-attachments/assets/b156303a-a9c1-48e6-be7d-0ef199dae49d" width="30" height="30" alt="Redis">
<img src="https://github.com/user-attachments/assets/2e144951-71fb-467d-8c0b-5bd8942cbc41" width="30" height="30" alt="Celery">
<img src="https://github.com/user-attachments/assets/8bf836d5-fa8c-4659-be79-8d5a298952e1" width="30" height="30" alt="RabbitMQ">
<img src="https://github.com/user-attachments/assets/4e2af97a-6d6f-470e-ab02-3eca1ca178ef" width="30" height="30" alt="Postgres">
<img src="https://github.com/user-attachments/assets/93cc82e1-00a9-4721-a494-f114f4576fd6" width="30" height="30" alt="Docker">
<img src="https://github.com/user-attachments/assets/b7a95aef-4eed-4f1a-b6e3-0b73dfd874eb" width="30" height="30" alt="Tailwind">

## Ferramentas de Desenvolvimento

<img src="https://github.com/user-attachments/assets/7f4a4f5d-8df4-40c4-b56a-004b2195426f" width="30" height="30" alt="Ubuntu">
<img src="https://github.com/user-attachments/assets/a488a309-43ac-4c00-899c-cb37de9ebf13" width="30" height="30" alt="Postman">
<img src="https://github.com/user-attachments/assets/e787007f-9215-4ba7-999e-8bd2e21548f6" width="30" height="30" alt="Github">
<img src="https://github.com/user-attachments/assets/e69015ce-0cbd-4d4d-979d-54653efc4eea" width="30" height="30" alt="Github Actions">
<img src="https://github.com/user-attachments/assets/51cc1f77-40eb-490d-bb88-3f1f1f376f7e" width="30" height="30" alt="MakeFile">
<img src="https://github.com/user-attachments/assets/6f153af7-19e4-4c0c-8c7a-2ecb700805f3" width="30" height="30" alt="VsCode">



---

## Como Rodar o Projeto

1. Crie um arquivo `.env` e preencha os dados que estão no arquivo `.env.example`.

2. Entre no seu ambiente virtual (venv). Exemplo para Ubuntu:

    ```bash
    . venv/bin/activate
    ```

3. Suba o Docker:

    ```bash
    make up
    ```

4. Execute as migrations:

    ```bash
    make migrations
    ```

5. Rode em um terminal o app:

    ```bash
    make run
    ```
    
6. Rode em outro terminal o celery:

    ```bash
    make celery
    ```

Se tudo correu bem, você verá a tela inicial:

<img src="https://github.com/user-attachments/assets/96fdec2e-24ad-4757-9cff-df97906a3b02" alt="API-Home" width="380" height="200">

7. Ficou com dúvida sobre algum comando? Execute:

    ```bash
    make help
    ```
    
---
## Driagrama de fluxo - Rotas

Estes diagramas oferecem uma visão clara e detalhada do fluxo de dados e das interações dentro da API, facilitando a análise, o acompanhamento e a gestão eficiente do sistema. A ferramenta utilizada para a criação desses diagramas foi o [Mermaid](https://mermaid.js.org/)
.

[![Ver Diagrama de fluxo](https://img.shields.io/badge/Ver_Diagrama_de_fluxo-Informational?style=for-the-badge&logo=mermaid&logoColor=white&color=D400CF)](/diagrams.md)

---
## WebHook Discord

Implementei um WebHook no Discord para receber notificações em tempo real sobre eventos do repositório, como commits, pull requests e o status da pipeline. Assim, posso acompanhar facilmente o progresso do projeto diretamente pelo Discord, centralizando a comunicação.


<img src="https://github.com/user-attachments/assets/399c6eec-8740-4572-9a8e-f55da1e90614" alt="WebHook Discord" width="600" height="600">

---

## Recursos Adicionais

Para entender melhor, criei alguns documentos no Notion que ajudam tanto iniciantes quanto pessoas que já estão usando Django e precisam tirar dúvidas sobre códigos.

[![Desenrolando Django](https://img.shields.io/badge/Desenrolando_Django-Informational?style=for-the-badge&logo=django&logoColor=white&color=%23006400)](https://cold-mailman-aa4.notion.site/Desenrolando-Django-8681c5f817a3476cbde317a5cac98739?pvs=74)
[![Desenrolando Redis](https://img.shields.io/badge/Desenrolando_Redis-Informational?style=for-the-badge&logo=django&logoColor=white&color=red)](https://cold-mailman-aa4.notion.site/Desenrolando-Redis-Django-10032fcdef508052a6bcdc874349fc57?pvs=74)
[![Desenrolando Celery com RabbitMQ](https://img.shields.io/badge/Desenrolando_Celery_com_RabbitMQ-Informational?style=for-the-badge&logo=celery&logoColor=white&color=orange)](https://cold-mailman-aa4.notion.site/Desenrolando-Celery-RabbitMQ-Django-20104b833b7848c28ba7d82d39b56e2b?pvs=4)
