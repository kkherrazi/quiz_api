
from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional, List
import pandas as pd

api = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")


class Quize(BaseModel):
    question: str
    subject: str
    correct: List[str]
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str] = None

class AdminQuize(Quize):
    admin_username: str
    admin_password: str

class QuizeListDescription(BaseModel):
    test_type: str
    categories: List[str]
    number_of_questions: int

# USERS DB 
USERS_DB = {
  "alice": "wonderland",
  "bob": "builder",
  "clementine": "mandarine"
}

@api.get('/verify', name="Verification de l'API")
def get_verify():
    """Vérifie que l'API est fonctionnelle
    """
    return {
        "message": "L'API est fonctionnelle"
    }


@api.post('/generate_quiz', name="Génèration des QCM ")
def generate_quiz(description: QuizeListDescription):
    """Génère un QCM basé sur les paramètres fournis.
    """
    return description


@api.post('/create_question', name="Creation de nouvel question ")
def create_quiz(quize: AdminQuize):
    """Crée une nouvelle question par un utilisateur admin.
    """
    return quize

 
def get_random_quizes(size: int):
    '''
    Fonction qui renvois N Quizes selectionneés aléatoirement à partire de la base de donné (le fichier CSV). 
    '''
    data = pd.read_csv("questions.csv")

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)

    # each time it gives 3 different rows
    return df.sample(n=size)


 