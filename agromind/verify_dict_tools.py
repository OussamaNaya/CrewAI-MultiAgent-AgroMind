#!/usr/bin/env python
"""
Test des outils au format dictionnaire pour CrewAI
"""

def test_dict_tool():
    """Test l'outil au format dictionnaire"""
    
    print("🧪 Test de l'outil au format dictionnaire...")
    
    try:
        from agromind.tools.classify_plant_by_api import classify_plant_tool_config
        print("✅ Configuration d'outil importée")
        
        # Vérification de la structure
        required_keys = ['name', 'description', 'function']
        for key in required_keys:
            if key in classify_plant_tool_config:
                print(f"✅ Clé '{key}' présente")
            else:
                print(f"❌ Clé '{key}' manquante")
                return False
        
        # Test de la fonction
        func = classify_plant_tool_config['function']
        result = func("test_image.jpg")
        print(f"✅ Test fonction réussi: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_agent_with_dict_tool():
    """Test création d'agent avec outil dictionnaire"""
    
    print("\n🤖 Test de création d'agent avec outil dictionnaire...")
    
    try:
        from crewai import Agent
        from agromind.tools.classify_plant_by_api import classify_plant_tool_config
        
        agent = Agent(
            role="Test Agent",
            goal="Test goal",
            backstory="Test backstory",
            tools=[classify_plant_tool_config],  # Format dictionnaire
            verbose=True
        )
        
        print("✅ Agent créé avec succès")
        print(f"✅ Nombre d'outils: {len(agent.tools)}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur création agent: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_crew_creation():
    """Test création du crew complet"""
    
    print("\n👥 Test de création du crew...")
    
    try:
        from agromind.crew import Agromind
        agromind = Agromind()
        print("✅ Crew créé avec succès")
        
        print(f"✅ Nombre d'agents: {len(agromind.agents)}")
        for i, agent in enumerate(agromind.agents):
            print(f"   Agent {i+1}: {agent.role} - {len(agent.tools) if agent.tools else 0} outils")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur création crew: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Test principal"""
    
    print("🚀 Test des outils au format dictionnaire\n")
    
    # Test 1: Outil dictionnaire
    dict_ok = test_dict_tool()
    if not dict_ok:
        print("\n❌ Problème avec l'outil dictionnaire. Arrêt.")
        return
    
    # Test 2: Agent avec outil dictionnaire
    agent_ok = test_agent_with_dict_tool()
    if not agent_ok:
        print("\n❌ Problème avec l'agent. Arrêt.")
        return
    
    # Test 3: Crew complet
    crew_ok = test_crew_creation()
    
    if dict_ok and agent_ok and crew_ok:
        print("\n🎉 Tous les tests sont passés !")
        print("✅ Vous pouvez maintenant exécuter: crewai run")
    else:
        print("\n❌ Des problèmes persistent.")

if __name__ == "__main__":
    main()