# 🌿 Agromind - Multi-Agent Plant Health Assistant

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://crewai.com)
[![YOLOv9](https://img.shields.io/badge/YOLOv9-Detection-orange.svg)](https://github.com/ultralytics/ultralytics)
[![Gradio](https://img.shields.io/badge/Gradio-Interface-purple.svg)](https://gradio.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Agromind est un assistant intelligent multi-agents basé sur **CrewAI**, conçu pour **identifier automatiquement les maladies des plantes** et fournir des **traitements efficaces et scientifiquement validés**. Le système s'adapte automatiquement à la langue de l'utilisateur (Français, Arabe, Anglais) et propose une interface utilisateur intuitive via Gradio.

> 🤖 **Technologie de pointe** : Architecture multi-agents CrewAI + YOLOv9 fine-tuné + Recherche web intelligente + Interface Gradio responsive

---

## ✨ Fonctionnalités principales

- 🔍 **Détection automatique** des maladies de plantes via deep learning (YOLOv9)
- 🌐 **Recherche intelligente** de traitements validés sur le web
- ✅ **Vérification scientifique** des remèdes proposés
- 🌍 **Support multilingue** automatique (FR/AR/EN)
- 📱 **Interface web intuitive** avec Gradio
- 🧠 **Architecture multi-agents** pour une analyse complète
- 📊 **Base de données** PlantVillage enrichie

---

## 🏗️ Architecture multi-agents CrewAI

### 🤖 Agent 1: `Classifier`
- **Mission** : Identification précise des maladies via analyse d'image
- **Technologie** : YOLOv9 fine-tuné sur [PlantVillage YOLO Dataset](https://www.kaggle.com/datasets/sebastianpalaciob/plantvillage-for-object-detection-yolo)
- **Sortie** : Label de maladie avec niveau de confiance

### 🔍 Agent 2: `Remedy Searcher`
- **Mission** : Recherche de traitements efficaces et durables
- **Outils** : Web search APIs, bases de données phytopathologiques
- **Focus** : Solutions biologiques et écologiques prioritaires

### ✅ Agent 3: `Remedy Verifier`
- **Mission** : Validation scientifique des traitements
- **Critères** : Efficacité, sécurité, impact environnemental
- **Méthode** : Analyse critique multi-sources

### 🌐 Agent 4: `Translator`
- **Mission** : Adaptation linguistique et culturelle
- **Capacités** : Détection automatique + traduction contextuelle
- **Langues** : Français, Arabe, Anglais (extensible)

---

## 🚀 Installation rapide

### Prérequis
- Python 3.8+
- Conda/pip
- GPU recommandé pour YOLO (optionnel)

### 1. Clonage du dépôt
```bash
git clone https://github.com/OussamaNaya/agromind.git
cd agromind
```

### 2. Environnement virtuel
```bash
# Avec conda (recommandé)
conda create -n agromind python=3.9
conda activate agromind

# Ou avec venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate    # Windows
```

### 3. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 4. Configuration (optionnel)
```bash
# Copier le fichier de configuration
cp config/config.example.yml config/config.yml
# Éditer selon vos besoins
```

---

## 💻 Utilisation

### Interface Gradio (Recommandé)
```bash
python app_ui.py
```
📡 **Interface accessible** : http://127.0.0.1:7860

### CLI (Command Line Interface)
```bash
python src/agromind/main.py --image path/to/plant_image.jpg --lang fr
```

### API Python
```python
from src.agromind.crew import AgroMindCrew

# Initialiser le système
crew = AgroMindCrew()

# Analyser une image
result = crew.analyze_plant_disease(
    image_path="plant_image.jpg",
    user_question="Quel traitement recommandez-vous ?",
    language="fr"
)

print(result.remedy)
```

---

## 🖼️ Exemple d'utilisation

### 📸 Input
- **Image** : Feuille de tomate avec taches brunes
- **Question** : "Comment traiter cette maladie naturellement ?"
- **Langue** : Français (détectée automatiquement)

### 🤖 Output
```
🔍 Maladie détectée : Mildiou de la tomate (Phytophthora infestans)
Confiance : 94.2%

💊 Traitement recommandé :
• Traitement préventif : Pulvérisation de bicarbonate de potassium (5g/L)
• Application : 2x/semaine le matin, éviter les heures chaudes
• Complément : Décoction de prêle (renforce les défenses naturelles)
• Prévention : Améliorer l'aération, éviter l'arrosage sur feuillage

⚠️ Attention : Traiter dès les premiers symptômes pour maximiser l'efficacité.

🌱 Alternative biologique : Trichoderma harzianum (champignon antagoniste)
```

---

## 📁 Structure du projet

```
agromind/
├── 📁 src/agromind/           # Code source principal
│   ├── main.py                # Point d'entrée CLI
│   ├── crew.py                # Architecture multi-agents
│   ├── agents/                # Définition des agents
│   ├── tools/                 # Outils (YOLO, web search, etc.)
│   └── utils/                 # Utilitaires
├── 📁 models/                 # Modèles YOLOv9 pré-entraînés
├── 📁 knowledge/              # Base de connaissances
├── 📁 config/                 # Fichiers de configuration
├── 📁 tests/                  # Tests unitaires et d'intégration
├── 📁 docs/                   # Documentation technique
├── app_ui.py                  # Interface Gradio
├── requirements.txt           # Dépendances Python
├── docker-compose.yml         # Déploiement containerisé
└── README.md                  # Ce fichier
```

---

## 🔧 Configuration avancée

### Variables d'environnement
```bash
# .env
OPENAI_API_KEY=your_openai_key
YOLO_MODEL_PATH=models/yolov9_plantvillage.pt
WEB_SEARCH_API_KEY=your_search_key
DEFAULT_LANGUAGE=fr
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines.

### Roadmap
- [ ] Support pour plus de cultures (fruits, légumes, céréales)
- [ ] Intégration base de données météo
- [ ] Application mobile (iOS/Android)
- [ ] API RESTful complète
- [ ] Système de feedback utilisateurs
- [ ] Intelligence artificielle prédictive

---

## 📜 Dépendances principales

| Package | Version | Usage |
|---------|---------|--------|
| `crewai` | ≥0.28.0 | Architecture multi-agents |
| `ultralytics` | ≥8.0.0 | YOLOv9 detection |
| `gradio` | ≥4.0.0 | Interface utilisateur |
| `langdetect` | ≥1.0.9 | Détection de langue |
| `requests` | ≥2.28.0 | Requêtes web |
| `Pillow` | ≥9.0.0 | Traitement d'images |
| `pandas` | ≥1.5.0 | Manipulation de données |

---

## 📄 Licence

Ce projet est sous licence **MIT**. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Oussama Naya**
- 🌐 [Portfolio](https://github.com/OussamaNaya)
- 💼 [LinkedIn](https://www.linkedin.com/in/oussama-naya-a4a398249/)
- 📧 [Email](mailto:oussamanaya8@gmail.com)
- 🐙 [GitHub](https://github.com/OussamaNaya)

---

## 🙏 Remerciements

- [PlantVillage Dataset](https://www.kaggle.com/datasets/sebastianpalaciob/plantvillage-for-object-detection-yolo) pour les données d'entraînement
- [CrewAI](https://crewai.com) pour le framework multi-agents
- [Ultralytics](https://ultralytics.com) pour YOLOv9
- [Gradio](https://gradio.app) pour l'interface utilisateur

---

## 📞 Support

Pour toute question ou problème :
- 🐛 [Issues GitHub](https://github.com/your-username/agromind/issues)
- 💬 [Discussions](https://github.com/your-username/agromind/discussions)
- 📧 Support direct : [support@agromind.com](mailto:oussamanaya8@gmail.com)

---

<div align="center">
  <p>Made with ❤️ for sustainable agriculture</p>
  <p>🌱 <strong>Agromind - Cultivating Intelligence for Healthier Plants</strong> 🌱</p>
</div>
