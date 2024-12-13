import re
import json

def contar_palavras_e_exibir_content(file_path, output_file):
    # Abre e lê o conteúdo do arquivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Define a expressão regular para capturar o conteúdo do campo "content"
    regex = r'"content"\s*:\s*"((?:[^"\\]|\\.)*?)"'

    # Encontra todas as ocorrências do campo "content"
    contents = re.findall(regex, data)

    # Remove quebras de linha explícitas (\n) e barras invertidas antes das aspas
    cleaned_contents = [re.sub(r'\\"', '"', re.sub(r'\\n', ' ', content)) for content in contents]

    # Abre o arquivo de saída para escrita
    with open(output_file, 'w', encoding='utf-8') as output:
        # Exibe o conteúdo de cada campo 'content' individualmente no arquivo
        for i, content in enumerate(cleaned_contents, 1):
            output.write(f"Box #{i}:\n")
            output.write(content + "\n")
            output.write("\n" + "-"*50 + "\n\n")  # Separador visual

        # Conta o número total de palavras nos conteúdos extraídos
        total_words = sum(len(content.split()) for content in cleaned_contents)
        output.write("Quantidade total de palavras nos campos 'content': " + str(total_words) + "\n")

    print(f"Conteúdo extraído e salvo em '{output_file}'")






















