import asyncio
import uuid

from genesis_agents.registry import ExampleGenesisAgent, AgentTask, AgentStatus


def test_example_agent_initialization_and_task_execution():
    async def run():
        agent = ExampleGenesisAgent()
        await agent.start()
        assert agent.status == AgentStatus.READY

        task = AgentTask(
            id=str(uuid.uuid4()),
            name="test_task",
            description="simple test",
            params={"message": "hello"},
        )

        result = await agent.execute_task(task)
        await agent.stop()

        assert result.success is True
        assert result.result["message"] == "hello"

    asyncio.run(run())
