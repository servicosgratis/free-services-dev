---
weight: 900
title: "Contribuindo"
description: "Contribua para a nossa comunidade melhorando a lista, aprimorando o código e ajudando outros desenvolvedores. Sua participação pode tornar recursos valiosos mais acessíveis para todos. Junte-se a nós na construção de um catálogo abrangente e confiável de serviços gratuitos!"
icon: "heart_plus"
date: "2024-11-17T05:12:51+01:00"
lastmod: "2024-11-17T05:12:51+01:00"
draft: false
toc: true
---

## Como Contribuir

Você pode contribuir para o **Serviços Grátis** de diversas formas! Se você encontrou um link quebrado, deseja adicionar um novo serviço ou fazer correções no conteúdo existente, a colaboração é muito bem-vinda!

### 1. Fazendo um Pull Request

A forma mais comum de contribuir é através de um **Pull Request (PR)**. Se você deseja adicionar ou atualizar informações, basta seguir estas etapas:

- Acesse o repositório no [GitHub](https://github.com/servicosgratis/free-services-dev).
- Faça um fork do repositório.
- Navegue até o arquivo YAML da página que deseja atualizar dentro da pasta **`data`**. Por exemplo:
  - **artificial-intelligence.yaml** para serviços de IA
  - **free-tier.yaml** para serviços no formato free-tier
  - **self-hosted.yaml** para serviços auto-hospedados
  - **sysadmin.yaml** para serviços de administração de sistemas
- Edite o arquivo YAML para adicionar ou corrigir o título, descrição, URL ou qualquer outra informação necessária.
- Faça um Pull Request com suas alterações e aguarde a revisão.

#### Estrutura da pasta data/:
```
data/
├── artificial-intelligence.yaml
├── free-tier.yaml
├── self-hosted.yaml
├── sysadmin.yaml
```

#### Exemplo de Estrutura YAML:
Cada arquivo YAML segue a seguinte estrutura:

```yaml
- title: "Título da categoria"
  sections:
    - title: "Título do serviço"
      url: "URL do site"
      description: "Descrição em inglês"
      pt: "Descrição em português"
```


### 2. Abrindo uma Issue

Se você encontrou um link quebrado ou não sabe exatamente como fazer a alteração, você pode abrir uma **Issue** no GitHub. Ao abrir uma issue, forneça o máximo de detalhes possível, como:

- O serviço ou página afetada.
- O link quebrado ou a informação incorreta.
- Sugestões para correções ou melhorias.

Para abrir uma issue, siga estas etapas:

- Acesse a página de **Issues** do repositório no [GitHub](https://github.com/servicosgratis/free-services-dev/issues).
- Clique em **New Issue**.
- Descreva o problema ou a melhoria que você deseja sugerir.

### 3. **Por que Contribuir?**

Ao contribuir com o projeto **Serviços Grátis**, você estará ajudando outros desenvolvedores e criadores de conteúdo a encontrar recursos valiosos de forma mais eficiente. Sua contribuição é importante para manter a lista atualizada e garantir que todos tenham acesso a informações precisas e úteis.

Agradecemos a sua colaboração!