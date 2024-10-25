def write_text_to_file(text, title, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(f"Titre : {title}\n\n")
        file.write(text)
