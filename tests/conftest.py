import sys
from pathlib import Path

# Ensure package is importable without installation
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / 'src'
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Provide a minimal stub for the optional ``mcpturbo`` dependency so
# the package can be imported in environments where it is missing.
import types
from enum import IntEnum

mcpturbo = types.ModuleType("mcpturbo")
mcpturbo_agents = types.ModuleType("mcpturbo.agents")
mcpturbo_types = types.ModuleType("mcpturbo.types")


class BaseAgent:
    def __init__(self, agent_id: str, capabilities):
        self.agent_id = agent_id
        self.capabilities = capabilities

    async def start(self):
        pass

    async def stop(self):
        pass


class TaskPriority(IntEnum):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


class AgentRegistry:
    def register(self, *args, **kwargs):
        pass

    def unregister(self, *args, **kwargs):
        pass


mcpturbo_agents.BaseAgent = BaseAgent
mcpturbo_agents.AgentRegistry = AgentRegistry
mcpturbo_types.TaskPriority = TaskPriority

mcpturbo.agents = mcpturbo_agents
mcpturbo.types = mcpturbo_types

sys.modules.setdefault("mcpturbo", mcpturbo)
sys.modules.setdefault("mcpturbo.agents", mcpturbo_agents)
sys.modules.setdefault("mcpturbo.types", mcpturbo_types)
