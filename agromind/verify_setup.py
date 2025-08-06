#!/usr/bin/env python
"""
Vérification rapide de la configuration Agromind
"""

def verify_imports():
    """Vérifie tous les imports nécessaires"""
    
    print("🔍 Vérification des imports...")
    
    # Test 1: Import de l'outil
    try:
        from agromind.tools.classify_plant_by_api import classify_plant_by_api
        print("✅ Outil classify_plant_by_api importé")
        print(f"   Type: {type(classify_plant_by_api)}")
        print(f"   Nom: {classify_plant_by_api.name}")
    except Exception as e:
        print(f"❌ Erreur import outil: {e}")
        return False
    
    # Test 2: Import CrewAI
    try:
        from crewai import Agent, Crew, Task
        print("✅ CrewAI importé")
    except Exception as e:
        print(f"❌ Erreur import CrewAI: {e}")
        return False
    
    # Test 3: Import crew
    try:
        from agromind.crew import Agromind
        print("✅ Agromind crew importé")
    except Exception as e:
        print(f"❌ Erreur import crew: {e}")
        return False
    
    return True

def test_tool_execution():
    """Teste l'exécution de l'outil"""
    
    print("\n🧪 Test d'exécution de l'outil...")
    
    try:
        from agromind.tools.classify_plant_by_api import classify_plant_by_api
        
        # Test d'exécution
        result = classify_plant_by_api.run("test_image.jpg")
        print(f"✅ Test réussi: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur test outil: {e}")
        return False

def test_agent_creation():
    """Teste la création d'un agent simple"""
    
    print("\n🤖 Test de création d'agent...")
    
    try:
        from crewai import Agent
        from agromind.tools.classify_plant_by_api import classify_plant_by_api
        
        agent = Agent(
            role="Test Agent",
            goal="Test goal",
            backstory="Test backstory",
            tools=[classify_plant_by_api],
            verbose=True
        )
        
        print("✅ Agent créé avec succès")
        print(f"   Nombre d'outils: {len(agent.tools)}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur création agent: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Fonction principale"""
    
    print("🚀 Vérification de la configuration Agromind\n")
    
    # Étape 1: Vérification des imports
    imports_ok = verify_imports()
    if not imports_ok:
        print("\n❌ Problème avec les imports. Arrêt.")
        return
    
    # Étape 2: Test de l'outil
    tool_ok = test_tool_execution()
    if not tool_ok:
        print("\n❌ Problème avec l'outil. Arrêt.")
        return
    
    # Étape 3: Test de création d'agent
    agent_ok = test_agent_creation()
    
    if imports_ok and tool_ok and agent_ok:
        print("\n🎉 Tous les tests sont passés !")
        print("✅ Vous pouvez maintenant exécuter: crewai run")
    else:
        print("\n❌ Des problèmes persistent.")

if __name__ == "__main__":
    main()