import openai
import time

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"

def generate_title(text):
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="openai/gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Générer un titre précis pour le texte suivant :"},
                    {"role": "user", "content": text}
                ],
                max_tokens=50,
            )
            return response.choices[0].message.content.strip()
        except openai.error.RateLimitError as e:
            print(f"Erreur de limite de taux : {e}")
            continue
        except Exception as e:
            print(f"Erreur lors de la génération du titre : {e}")
            break
