import pytest
import asyncio

@pytest.mark.asyncio
async def test_super_basic():
    """Test más simple posible"""
    await asyncio.sleep(0.001)
    assert True

def test_sync():
    """Test síncrono para comparar"""
    assert True
