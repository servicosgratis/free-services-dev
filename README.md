# Free Services

## [Artificial Intelligence (AI)](artificial-intelligence_en.md)
## [Free-Tier](free-tier_en.md)

# About Free Services - English
[Free Services](https://freeservices.dev) is a catalog of free services for developers, including **free-tier** options on SaaS, PaaS, and IaaS platforms as well as **self-hosted** **open-source** solutions that can be installed and run locally or on private servers. Originally created in 2000, Free Services was one of the first sites dedicated to listing free tools on the internet, and it is now being revamped to meet the needs of today’s developers, evolving into a fully open-source project.

## Purpose
This project aims to make free tools more accessible for development, testing, and deployment, supporting the developer community with options that are both accessible and easy to implement. Our goal is not only to list services with free tiers but also to promote open-source alternatives for independent use.

## Contributing
The developer community is encouraged to contribute to expand and keep the catalog up to date. If you know of a free service or tool that isn’t listed, feel free to open a pull request or issue.

## How to Contribute
### 1. Making a Pull Request

The most common way to contribute is by submitting a **Pull Request (PR)**. If you'd like to add or update information, simply follow these steps:

- Go to the repository on [GitHub](https://github.com/servicosgratis/free-services-dev).
- Fork the repository.
- Navigate to the YAML file for the page you want to update within the **`data`** folder. For example:
  - **artificial-intelligence.yaml** for AI services
  - **free-tier.yaml** for free-tier services
  - **self-hosted.yaml** for self-hosted services
  - **sysadmin.yaml** for sysadmin services
- Edit the YAML file to add or correct the title, description, URL, or any other necessary information.
- Submit a Pull Request with your changes and wait for review.

#### data/ folder structure:
```
data/
├── artificial-intelligence.yaml
├── free-tier.yaml
├── self-hosted.yaml
├── sysadmin.yaml
```

#### Example YAML Structure:
Each YAML file follows this structure:

```yaml
- title: "Category Title"
  sections:
    - title: "Service Title"
      url: "Service URL"
      description: "Description in English"
      pt: "Description in Portuguese"
```

### 2. Opening an Issue

If you have found a broken link or aren't sure how to make the change, you can open an **Issue** on GitHub. When opening an issue, please provide as much detail as possible, such as:

- The affected service or page.
- The broken link or incorrect information.
- Suggestions for corrections or improvements.

To open an issue, follow these steps:

- Go to the **Issues** page of the repository on [GitHub](https://github.com/servicosgratis/free-services-dev/issues).
- Click on **New Issue**.
- Describe the problem or improvement you would like to suggest.

## Websites
- [LetsCloud](https://letscloud.io) - Cloud Servers made for developers
- [iMasters](https://imasters.com.br) - Developer Community
- [Reddit](https://reddit.com) - Home to thousands of communities.
  -  [/r/Developers](https://www.reddit.com/r/developers/) - Developer Community
  -  [/r/Devops](https://www.reddit.com/r/devops/) - Everything DevOps
  -  [/r/SelfHosted](https://www.reddit.com/r/selfhosted/) - Self-Hosted Alternatives to Popular Services
