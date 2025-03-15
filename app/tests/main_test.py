from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_verify():
    response = client.get("/verify")
    assert response.status_code == 200
    assert response.json().get("message")  != ""