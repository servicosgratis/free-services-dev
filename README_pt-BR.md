# Serviços Grátis

## [Artificial Intelligence (AI)](artificial-intelligence_pt-BR.md)
## [Free-Tier](free-tier_pt-BR.md)

# Sobre Serviços Grátis
[Serviços Grátis](https://servicosgratis.com.br) é um catálogo de serviços gratuitos para desenvolvedores, incluindo desde free-tier em plataformas SaaS, PaaS e IaaS até soluções self-hosted open-source que podem ser instaladas e executadas localmente ou em servidores próprios. Criado originalmente em 2000, Serviços Grátis foi um dos primeiros sites dedicados a listar ferramentas gratuitas na internet e, está sendo reformulado para atender às necessidades dos desenvolvedores atuais e se tornando um projeto completamente open-source.

## Objetivo
Este projeto tem como objetivo facilitar o acesso a ferramentas gratuitas para desenvolvimento, testes e implantação, apoiando a comunidade de desenvolvedores com opções acessíveis e de fácil implementação. Nossa ideia é não apenas listar serviços que oferecem tiers gratuitos, mas também promover alternativas open-source para uso independente.

## Contribuição
A comunidade de desenvolvedores é incentivada a contribuir para expandir e manter o catálogo atualizado. Se você conhece um serviço ou ferramenta gratuita que não está listado, sinta-se à vontade para abrir uma pull request ou issue.

## Como Contribuir
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


## Websites
- [LetsCloud](https://letscloud.io) - Servidores de Cloud feito para desenvolvedores
- [iMasters](https://imasters.com.br) - Comunidade de desenvolvedores
- [Reddit](https://reddit.com) - Casa para milhares de comunidades.
  -  [/r/Developers](https://www.reddit.com/r/developers/) - Comunidade de desenvolvedores
  -  [/r/Devops](https://www.reddit.com/r/devops/) - Tudo sobre DevOps
  -  [/r/SelfHosted](https://www.reddit.com/r/selfhosted/) - Self-Hosted alternative para Serviços Populares
