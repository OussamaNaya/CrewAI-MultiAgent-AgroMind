#!/usr/bin/env python
"""
Test final avec le bon import de BaseTool
"""

def test_correct_basetool():
    """Test avec crewai.tools.BaseTool"""
    
    print("🧪 Test avec crewai.tools.BaseTool...")
    
    try:
        # Import de BaseTool depuis le bon module
        from crewai.tools import BaseTool
        print("✅ BaseTool importé depuis crewai.tools")
        
        # Import de notre outil
        from agromind.tools.classify_plant_by_api import classify_plant_by_api
        print("✅ Outil classify_plant_by_api importé")
        
        # Vérification que c'est bien une instance de BaseTool
        if isinstance(classify_plant_by_api, BaseTool):
            print("✅ L'outil hérite bien de crewai.tools.BaseTool")
        else:
            print(f"❌ L'outil n'hérite pas de BaseTool: {type(classify_plant_by_api)}")
            return False
        
        # Vérification des attributs
        print(f"✅ Nom: {classify_plant_by_api.name}")
        print(f"✅ Description: {classify_plant_by_api.description}")
        
        # Test d'exécution
        result = classify_plant_by_api._run("test_image.jpg")
        print(f"✅ Test exécution réussi: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_agent_creation_final():
    """Test final de création d'agent"""
    
    print("\n🤖 Test final de création d'agent...")
    
    try:
        from crewai import Agent
        from agromind.tools.classify_plant_by_api import classify_plant_by_api
        
        agent = Agent(
            role="Plant Disease Classifier",
            goal="Classify plant diseases from images",
            backstory="Expert in plant pathology with access to classification tools",
            tools=[classify_plant_by_api],
            verbose=True
        )
        
        print("✅ Agent créé avec succès !")
        print(f"✅ Nombre d'outils: {len(agent.tools)}")
        print(f"✅ Type de l'outil: {type(agent.tools[0])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_full_crew():
    """Test du crew complet"""
    
    print("\n👥 Test du crew complet...")
    
    try:
        from agromind.crew import Agromind
        
        print("🚀 Création du crew...")
        agromind = Agromind()
        print("✅ Crew créé avec succès")
        
        print(f"✅ Nombre d'agents: {len(agromind.agents)}")
        for i, agent in enumerate(agromind.agents):
            tools_count = len(agent.tools) if agent.tools else 0
            print(f"   Agent {i+1}: {agent.role} - {tools_count} outils")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Test principal"""
    
    print("🚀 Test final avec crewai.tools.BaseTool\n")
    
    # Test 1: BaseTool correct
    basetool_ok = test_correct_basetool()
    if not basetool_ok:
        print("\n❌ Problème avec BaseTool. Arrêt.")
        return
    
    # Test 2: Agent
    agent_ok = test_agent_creation_final()
    if not agent_ok:
        print("\n❌ Problème avec l'agent. Arrêt.")
        return
    
    # Test 3: Crew complet
    crew_ok = test_full_crew()
    
    if basetool_ok and agent_ok and crew_ok:
        print("\n🎉 TOUS LES TESTS SONT PASSÉS !")
        print("✅ Votre configuration est maintenant correcte")
        print("✅ Vous pouvez exécuter: crewai run")
    else:
        print("\n❌ Des problèmes persistent.")

if __name__ == "__main__":
    main()