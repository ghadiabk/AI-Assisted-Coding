"""
Pytest configuration for Task Tracker tests.
Provides fixtures for testing.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.storage import _reset


@pytest.fixture(scope="function", autouse=True)
def reset_storage():
    """Reset storage before each test."""
    _reset()
    yield
    _reset()


@pytest.fixture(scope="function")
def client():
    """Provide a test client for API testing."""
    return TestClient(app)
