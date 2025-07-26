import asyncio
import unittest

class TestManual(unittest.TestCase):
    def test_async_manual(self):
        """Test sin pytest-asyncio"""
        async def async_func():
            await asyncio.sleep(0.001)
            return "success"

        # Ejecutar manualmente
        result = asyncio.run(async_func())
        self.assertEqual(result, "success")
