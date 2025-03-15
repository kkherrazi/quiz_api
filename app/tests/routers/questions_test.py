from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_when_create_question_whith_wrong_admin_password_then_ok():
    headers = {"Content-Type":"application/json"}
    data={
    "admin_username": "admin",
    "admin_password": "un_bon_password",
    "question": "Quelle est la capitale de la France ?",
    "subject": "geography",
    "correct": ["Paris"],
    "use": "multiple_choice",
    "responseA": "Londres",
    "responseB": "Paris",
    "responseC": "Berlin",
    "responseD": "Madrid"
  }
    response = client.post("/create_question", headers=headers, json=data)
    assert response.status_code == 201


def test_when_create_question_with_good_admin_password_then_nok():
    headers = {"Content-Type":"application/json"}
    data={
    "admin_username": "admin",
    "admin_password": "movais_password",
    "question": "Quelle est la capitale de la France ?",
    "subject": "geography",
    "correct": ["Paris"],
    "use": "multiple_choice",
    "responseA": "Londres",
    "responseB": "Paris",
    "responseC": "Berlin",
    "responseD": "Madrid"
  }
    response = client.post("/create_question", headers=headers, json=data)
    assert response.status_code == 401   


    
    