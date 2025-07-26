# tests/test_communication.py

import asyncio
import unittest
from genesis_agents.communication import queue_manager

class TestCommunication(unittest.TestCase):
    def setUp(self):
        """
        Reset the queue manager before each test.
        """
        queue_manager.queues = {}

    def test_create_and_get_queue(self):
        """
        Test creating and getting a queue.
        """
        queue_manager.create_queue("test_queue")
        queue = queue_manager.get_queue("test_queue")
        self.assertIsInstance(queue, asyncio.Queue)

    def test_get_nonexistent_queue(self):
        """
        Test getting a non-existent queue.
        """
        with self.assertRaises(KeyError):
            queue_manager.get_queue("nonexistent_queue")

    def test_publish_and_subscribe(self):
        """
        Test publishing and subscribing to a queue.
        """
        async def run_test():
            queue_manager.create_queue("test_queue")
            message = {"data": "test_message"}
            await queue_manager.publish("test_queue", message)
            received_message = await queue_manager.subscribe("test_queue")
            self.assertEqual(received_message, message)

        asyncio.run(run_test())

    def test_subscribe_from_empty_queue(self):
        """
        Test subscribing from an empty queue.
        """
        async def run_test():
            queue_manager.create_queue("test_queue")
            task = asyncio.create_task(queue_manager.subscribe("test_queue"))
            await asyncio.sleep(0.1)
            self.assertFalse(task.done())
            await queue_manager.publish("test_queue", "message")
            await asyncio.sleep(0.1)
            self.assertTrue(task.done())
            self.assertEqual(await task, "message")

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
