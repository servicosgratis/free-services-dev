import os
import yaml

def yaml_to_markdown(input_folder, output_folder):
    # Garantir que a pasta de saída exista
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".yaml"):
            # Caminho completo para o arquivo YAML
            yaml_file = os.path.join(input_folder, file_name)

            # Nome do arquivo .md baseado no arquivo .yaml
            base_name = os.path.splitext(file_name)[0]
            output_md_english = os.path.join(output_folder, f"{base_name}_en.md")
            output_md_portuguese = os.path.join(output_folder, f"{base_name}_pt-BR.md")

            # Processar o arquivo YAML
            with open(yaml_file, 'r') as file:
                data = yaml.safe_load(file)

            # Gerar arquivos em inglês e português
            with open(output_md_english, 'w') as md_english:
                for item in data.get('items', []):
                    md_english.write(f"## {item['title']}\n")
                    for section in item.get('sections', []):
                        md_english.write(f"  * [{section['title']}]({section['url']}) — {section['description']}\n")
                    md_english.write("\n")

            with open(output_md_portuguese, 'w') as md_portuguese:
                for item in data.get('items', []):
                    md_portuguese.write(f"## {item['title']}\n")
                    for section in item.get('sections', []):
                        md_portuguese.write(f"  * [{section['title']}]({section['url']}) — {section['pt']}\n")
                    md_portuguese.write("\n")

# Exemplo de uso
yaml_to_markdown("data", ".")
