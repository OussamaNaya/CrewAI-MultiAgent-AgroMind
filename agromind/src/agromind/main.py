#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from agromind.crew import Agromind

# Pour la détection de langue
try:
    from langdetect import detect
except ImportError:
    print("langdetect non installé. Installation: pip install langdetect")
    sys.exit(1)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def detect_language(question: str) -> str:
    """Détecte la langue de la question utilisateur"""
    try:
        lang = detect(question)
        print(f'\n🔍 Langue détectée: {lang}\n')
        
        # Mapping des codes de langue
        language_map = {
            'fr': 'fr',  # français
            'ar': 'ar',  # arabe
            'en': 'en'   # anglais
        }
        
        return language_map.get(lang, 'en')  # anglais par défaut
    except Exception as e:
        print(f"⚠️ Erreur de détection de langue: {e}. Utilisation de l'anglais par défaut.")
        return 'en'

def run():
    """
    Exécute le crew Agromind avec une image et une question utilisateur.
    Le système détecte automatiquement la langue de la question.
    """
    # Configuration par défaut - modifiez selon vos besoins
    # image_url = "C:/Users/LENOVO/Documents/Groupe OMF/FSBM/Image Classification/Deploimenet avec Gradio/plantvillage_dataset/PlantVillage_for_object_detection/Dataset/images/APBR_image (55).jpg"
    image_url = "C:/Users/LENOVO/Documents/Groupe OMF/FSBM/Image Classification/Deploimenet avec Gradio/plantvillage_dataset/PlantVillage_for_object_detection/Dataset/images/TMTS_image (220).jpg"
    # user_question = "ما هو علاج هذا المرض؟"  # Question en arabe
    user_question = "Quel est le traitement de cette maladie ?" # Question en francais
    
    # Vérifier si l'image existe
    if not os.path.exists(image_url):
        print(f"⚠️ Attention: Le fichier image n'existe pas à: {image_url}")
        print("Le processus continuera avec l'URL fournie...")
    
    # Détection de la langue
    detected_language = detect_language(user_question)
    
    # Préparation des inputs pour le crew
    inputs = {
        "image_url": image_url,
        "question": user_question,
        "language": detected_language,
        "current_year": str(datetime.now().year)
    }
    
    print("🚀 Démarrage d'Agromind...")
    print(f"📸 Image: {image_url}")
    print(f"❓ Question: {user_question}")
    print(f"🌐 Langue: {detected_language}")
    print("-" * 50)
    
    try:
        # Initialisation et exécution du crew
        agromind_crew = Agromind()
        result = agromind_crew.crew().kickoff(inputs=inputs)
        
        print("\n" + "="*50)
        print("🧠 RÉPONSE D'AGROMIND:")
        print("="*50)
        print(result)
        print("="*50)
        
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution du crew: {e}")
        print(f"Type d'erreur: {type(e).__name__}")
        import traceback
        traceback.print_exc()

def train():
    """Entraîne le crew pour un nombre donné d'itérations"""
    if len(sys.argv) < 3:
        print("Usage: python main.py train <n_iterations> <filename>")
        return
        
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    
    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        Agromind().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        print(f"❌ Erreur lors de l'entraînement: {e}")

def replay():
    """Rejoue l'exécution du crew depuis une tâche spécifique"""
    if len(sys.argv) < 2:
        print("Usage: python main.py replay <task_id>")
        return
        
    try:
        task_id = sys.argv[1]
        Agromind().crew().replay(task_id=task_id)
    except Exception as e:
        print(f"❌ Erreur lors du replay: {e}")

def test():
    """Teste l'exécution du crew et retourne les résultats"""
    if len(sys.argv) < 3:
        print("Usage: python main.py test <n_iterations> <eval_llm>")
        return
        
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        n_iterations = int(sys.argv[1])
        eval_llm = sys.argv[2]
        Agromind().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "train":
            train()
        elif command == "replay":
            replay()
        elif command == "test":
            test()
        else:
            print("Commandes disponibles: train, replay, test")
            print("Exécution normale...")
            run()
    else:
        run()