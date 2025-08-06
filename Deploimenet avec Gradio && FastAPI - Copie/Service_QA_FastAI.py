from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import shutil
import os

# Initialisation FastAPI
app = FastAPI()

# Liste des noms (indexés de 0 à 37)
disease_names = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy", "Cherry___Powdery_mildew", "Cherry___healthy",
    "Corn___Cercospora_leaf_spot Gray_leaf_spot", "Corn___Common_rust", "Corn___Northern_Leaf_Blight",
    "Corn___healthy", "Grape___Black_rot", "Grape___Esca_(Black_Measles)", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy", "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot", "Peach___healthy",
    "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy", "Potato___Early_blight", "Potato___Late_blight",
    "Potato___healthy", "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch", "Strawberry___healthy", "Tomato___Bacterial_spot", "Tomato___Early_blight",
    "Tomato___Late_blight", "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus", "Tomato___healthy"
]

# Charger le modèle
model = YOLO('./best_v8.pt')

# Fonction de classification
def Yolov9_Classification(image_path):
    results = model(image_path)
    cls_id = int(results[0].boxes.cls[0].item())
    conf = results[0].boxes.conf[0].item()
    return disease_names[cls_id], float(conf)

# Endpoint API
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Sauvegarde temporaire
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        label, confidence = Yolov9_Classification(temp_file)
        os.remove(temp_file)  # Nettoyage
        return JSONResponse(content={"class": label, "confidence": confidence})
    except Exception as e:
        os.remove(temp_file)
        return JSONResponse(content={"error": str(e)}, status_code=500)
