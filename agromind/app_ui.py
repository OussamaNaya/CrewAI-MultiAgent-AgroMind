import gradio as gr
from datetime import datetime
from langdetect import detect
from src.agromind.crew import Agromind  # 🔥 chemin correct
import os

# Détecte la langue
def detect_language(question: str) -> str:
    try:
        lang = detect(question)
        return {'fr': 'fr', 'ar': 'ar', 'en': 'en'}.get(lang, 'en')
    except:
        return 'en'

# Fonction appelée par Gradio
def agromind_ui(image, question):
    if image is None or not question.strip():
        return "❌ Veuillez fournir une image et une question."

    try:
        image_path = image
        lang = detect_language(question)

        inputs = {
            "image_url": image_path,
            "question": question,
            "language": lang,
            "current_year": str(datetime.now().year)
        }

        print("🚀 Démarrage d'Agromind...")
        print(f"📸 Image: {image_path}")
        print(f"❓ Question: {question}")
        print(f"🌐 Langue: {lang}")
        print("-" * 50)

        agromind_crew = Agromind()
        result = agromind_crew.crew().kickoff(inputs=inputs)

        return f"🧠 Réponse d'Agromind :\n\n{result}"

    except Exception as e:
        return f"❌ Erreur : {str(e)}"


# Interface Gradio
demo = gr.Interface(
    fn=agromind_ui,
    inputs=[
        gr.Image(type="filepath", label="📸 Télécharger une image de plante"),
        gr.Textbox(label="❓ Posez votre question (ar/fr/en)")
    ],
    outputs="text",
    title="🌿 Agromind - Diagnostic intelligent",
    description="Détecte la maladie d'une plante avec CrewAI à partir d'une image + question."
)


if __name__ == "__main__":
    demo.launch()
