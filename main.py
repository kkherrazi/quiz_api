
from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional, List
import pandas as pd
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
 

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
def generate_quiz(desc: QuizeListDescription):
    """Génère un QCM basé sur les paramètres fournis.
    """
    return get_random_quizes(desc.number_of_questions, desc.categories, desc.test_type)


@api.post('/create_question', name="Creation de nouvel question ")
def create_quiz(quize: AdminQuize):
    """Crée une nouvelle question par un utilisateur admin.
    """
    return quize

 
def get_random_quizes(size: int,  categories: List[str], test_type: str ) :
    '''
    Fonction qui renvois N Quizes selectionneés aléatoirement à partire de la base de donné (le fichier CSV). 
    '''
    # read csv file 
    df = pd.read_csv("questions.csv")
    
    #filter data 
    df = df.query('use == @test_type and subject in @categories')

    # geta random list
    df = df.sample(n=size) 

    df = df.to_json(orient="records") 
    print(df)

    #json_compatible_item_data = jsonable_encoder(df)
    return JSONResponse(content=df)
    #return df
    

res = get_random_quizes(1, ["Classification", "Automation"], "Test de validation" )
print(res)