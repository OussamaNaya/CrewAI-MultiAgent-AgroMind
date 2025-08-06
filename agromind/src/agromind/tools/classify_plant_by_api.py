from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
# from tokenizers import Tokenizer
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Liste des noms (indexés de 0 à 37)
disease_names = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry___Powdery_mildew",
    "Cherry___healthy",
    "Corn___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn___Common_rust",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy", 
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

# Charger le modèle entraîné
model = YOLO('C:/Users/LENOVO/Documents/Groupe OMF/FSBM/Image Classification/Deploimenet avec Gradio/best_v8.pt')  # Le chemin peut changer selon le nom du dossier

def Yolov9_Classification(image_path):
    # Faire une prédiction
    results = model(image_path)

    # Affichage personnalisé avec noms
    cls_id = int(results[0].boxes.cls[0].item())
    conf = results[0].boxes.conf[0].item()

    return disease_names[cls_id]

class ClassifyPlantInput(BaseModel):
    """Input schema for classify_plant_by_api"""
    image_url: str = Field(..., description="The URL or path to the plant image to classify")


class ClassifyPlantByApiTool(BaseTool):
    name: str = "classify_plant_by_api"
    description: str = (
        "Classify plant diseases from an image URL using an external API. "
        "Provide the URL or path to the plant image to get disease classification."
    )
    args_schema: Type[BaseModel] = ClassifyPlantInput

    def _run(self, image_url: str) -> str:
        """
        Classify plant diseases from an image URL.
        
        Args:
            image_url (str): The URL or path to the plant image to classify
            
        Returns:
            str: The identified disease name (e.g., 'Tomato___Late_blight')
        """
        try:
            # Vérifier si c'est un chemin local ou une URL
            if os.path.exists(image_url):
                print(f"[DEBUG] Traitement de l'image locale: {image_url}")
            else:
                print(f"[DEBUG] Traitement de l'URL d'image: {image_url}")
            
            # Simulation d'appel API - Remplacez par votre vraie API
            print(f"[DEBUG] Classification simulée pour: {image_url}")
            
            # Retour simulé avec plus de détails
            # return "Tomato___Late_blight (Confidence: 95%)"
            return Yolov9_Classification(image_url)
            
        except Exception as e:
            print(f"[ERROR] Erreur lors de la classification: {e}")
            return f"Classification_failed: {str(e)}"


# Créer une instance de l'outil
classify_plant_by_api = ClassifyPlantByApiTool()