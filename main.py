import os
import glob
from extract_text import extract_text_from_image
from generate_title import generate_title
from write_text import write_text_to_file

image_folder_path = r"GeneratedImages"

output_folder_path = r"textes"

image_files = glob.glob(os.path.join(image_folder_path, '*.png')) + \
              glob.glob(os.path.join(image_folder_path, '*.jpg')) + \
              glob.glob(os.path.join(image_folder_path, '*.jpeg')) + \
              glob.glob(os.path.join(image_folder_path, '*.bmp')) + \
              glob.glob(os.path.join(image_folder_path, '*.gif'))
os.makedirs(output_folder_path, exist_ok=True)

for image_path in image_files:
    text = extract_text_from_image(image_path)
    title = generate_title(text)
    output_file_name = os.path.splitext(os.path.basename(image_path))[0] + '.txt'
    output_path = os.path.join(output_folder_path, output_file_name)
    write_text_to_file(text, title, output_path)
    print(f"Texte extrait de {os.path.basename(image_path)} et enregistré dans {output_file_name}")

print("Extraction de texte et génération de titres terminée.")
