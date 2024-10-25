import os
from PIL import Image, ImageDraw
import random

output_folder_path = r"GeneratedImages"
os.makedirs(output_folder_path, exist_ok=True)

def generate_image(image_path):
    width, height = 800, 600  
    image = Image.new('RGB', (width, height), (255, 255, 255))  
    draw = ImageDraw.Draw(image)

    for _ in range(10):  
        shape_type = random.choice(['rectangle', 'ellipse', 'line'])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if shape_type == 'rectangle' or shape_type == 'ellipse':
            x1, y1 = random.randint(0, width // 2), random.randint(0, height // 2)
            x2, y2 = x1 + random.randint(0, width // 2), y1 + random.randint(0, height // 2)
            if shape_type == 'rectangle':
                draw.rectangle([x1, y1, x2, y2], fill=color)
            else:
                draw.ellipse([x1, y1, x2, y2], fill=color)
        elif shape_type == 'line':
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            draw.line([x1, y1, x2, y2], fill=color, width=5)

    image.save(image_path)
for i in range(1, 3):
    image_path = os.path.join(output_folder_path, f"image_{i}.png")
    generate_image(image_path)
    print(f"Image {i} générée et enregistrée dans {image_path}")

print("Génération des images terminée.")
