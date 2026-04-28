import sys
import os

sys.path.append(os.path.abspath("."))

from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_health():
    assert client.get("/health").status_code == 200


def test_ready():
    assert client.get("/ready").status_code == 200


def test_home():
    assert client.get("/").status_code == 200
