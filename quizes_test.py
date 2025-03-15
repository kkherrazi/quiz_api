from fastapi import FastAPI
from fastapi.testclient import TestClient
import json
from main import api

client = TestClient(api)

AUTH_HEADER_OK  = "Basic a2hhbGlkOmtoZXJyYXpp"  # khalid:kherrazi
AUTH_HEADER_NOK = "Basic dGVzdDp0ZXN0"          # test:test

def test_when_generate_quiz_then_ok():
    headers = {"Authorization": "Basic a2hhbGlkOmtoZXJyYXpp", "Content-Type":"application/json"}
    json={
      "test_type": "Test de validation",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 4
    }
    response = client.post("/generate_quiz", headers=headers, json=json)
    assert response.status_code == 200
    assert response.json

def test_when_generate_quiz_with_wrong_credentials_then_nok():
    headers = {"Authorization": AUTH_HEADER_NOK, "Content-Type":"application/json"}
    data={
      "test_type": "Test de validation",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 4
    }
    response = client.post("/generate_quiz", headers=headers, json=data)
    assert response.status_code == 401

def test_when_generate_quiz_with_empty_test_type_then_nok():
    headers = {"Authorization": AUTH_HEADER_OK, "Content-Type":"application/json"}
    data={
      "categories": ["Automation", "Classification"],
      "number_of_questions": 4
    }
    response = client.post("/generate_quiz", headers=headers, json=data)
    assert response.status_code == 422

def test_when_generate_quiz_then_return_random_list():
    headers = {"Authorization": AUTH_HEADER_OK, "Content-Type":"application/json"}
    data={
      "test_type": "Test de validation",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 10
    }
    response1 = client.post("/generate_quiz", headers=headers, json=data)
    assert response1.status_code == 200
    response2 = client.post("/generate_quiz", headers=headers, json=data)
    assert response1.status_code == 200
    assert response1.json() != response2.json()   

def test_when_generate_quiz_with_number_of_questions_eq_0_then_nok():
    headers = {"Authorization": AUTH_HEADER_OK, "Content-Type":"application/json"}
    data={
      "test_type": "Test de validation",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 0
    }
    response = client.post("/generate_quiz", headers=headers, json=data)
    assert response.status_code == 422

def test_when_generate_quiz_with_number_of_questions_eq_100_then_nok():
    headers = {"Authorization": AUTH_HEADER_OK, "Content-Type":"application/json"}
    data={
      "test_type": "Test de validation",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 0
    }
    response = client.post("/generate_quiz", headers=headers, json=data)
    assert response.status_code == 422    
    
    