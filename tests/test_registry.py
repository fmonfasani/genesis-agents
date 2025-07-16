from genesis_agents.registry import (
    GenesisAgentRegistry,
    ExampleGenesisAgent,
    AgentCapability,
)


def test_registry_manual_registration():
    registry = GenesisAgentRegistry()
    agent = ExampleGenesisAgent()
    registry.register_agent(agent)

    assert registry.get_agent(agent.agent_id) is agent
    assert agent.agent_id in registry.list_agents()
    assert AgentCapability.ARCHITECTURE_DESIGN in registry.list_available_capabilities()


def test_registry_discovery():
    registry = GenesisAgentRegistry()
    registry.discover_and_register_agents(["genesis_agents.base.genesis_agent"])

    agent = registry.get_agent("example_agent")
    assert isinstance(agent, ExampleGenesisAgent)
    assert "genesis_agents.base.genesis_agent" in registry.discovered_modules
