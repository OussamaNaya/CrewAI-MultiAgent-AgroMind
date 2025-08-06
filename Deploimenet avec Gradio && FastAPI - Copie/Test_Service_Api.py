import requests

# URL de l'API FastAPI (assure-toi qu'elle est bien en cours d'exécution)
url = "http://127.0.0.1:8000/predict/"

# Chemin vers ton image de test
image_path = "C:/Users/LENOVO/Documents/Groupe OMF/FSBM/Image Classification/Deploimenet avec Gradio/plantvillage_dataset/PlantVillage_for_object_detection/Dataset/images/TMTS_image (220).jpg"

# Préparer les données
with open(image_path, "rb") as image_file:
    files = {"file": (image_path.split("/")[-1], image_file, "image/jpeg")}
    response = requests.post(url, files=files)

# Résultat
print("Statut HTTP :", response.status_code)
print("Réponse JSON :", response.json())
