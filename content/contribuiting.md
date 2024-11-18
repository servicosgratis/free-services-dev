---
weight: 900
title: "Contributing"
description: "Contribute to our community by improving the list, enhancing code, and helping fellow developers. Your input can make valuable resources more accessible for everyone. Join us in building a comprehensive, reliable catalog of free services!"
icon: "heart_plus"
date: "2024-11-17T05:12:51+01:00"
lastmod: "2024-11-17T05:12:51+01:00"
draft: false
toc: true
---

## How to Contribute

You can contribute to **Free Services** in several ways! If you've found a broken link, want to add a new service, or make corrections to existing content, your collaboration is highly welcome!

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

### 3. **Why Contribute?**

By contributing to the **Free Services** project, you'll help other developers and content creators find valuable resources more efficiently. Your contribution is important to keep the list updated and ensure everyone has access to accurate and useful information.

Thank you for your collaboration!