from fastapi import FastAPI, APIRouter, HTTPException, Response, status, Depends, HTTPException
from fastapi import Header
from pydantic import BaseModel
from typing import Optional, List
import pandas as pd
 
from fastapi.responses import JSONResponse

from dependencies import verify_authorization_header


class Quize(BaseModel):
    """Represente un Quiz.
    """
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
    """Description d'une list de Quiz
    """
    test_type: str
    categories: List[str]
    number_of_questions: int

unauthenticated_router = APIRouter() 

authenticated_router = APIRouter(
    dependencies=[Depends(verify_authorization_header)],
    responses={404: {"description": "Not found"}},
    )  

@unauthenticated_router.get('/verify', name="Verification de l'API")
def get_verify():
    """Vérifie que l'API est fonctionnelle
    """
    return {
        "message": "L'API est fonctionnelle"
    }
 
@authenticated_router.post('/generate_quiz', name="Génèration des QCM " )
def generate_quiz(desc: QuizeListDescription ):
    """Génère un QCM basé sur les paramètres fournis.
    """
    return get_random_quizes(desc.number_of_questions, desc.categories, desc.test_type)

ADMIN_USER = {
  "admin_username": "admin",
  "admin_password": "un_bon_password"
}

@unauthenticated_router.post('/create_question', name="Creation de nouvel question ")
def create_question(quize: AdminQuize,  response: Response): 
    """Crée une nouvelle question par un utilisateur admin.
    """
    if ADMIN_USER["admin_username"]!=quize.admin_username or ADMIN_USER["admin_password"]!=quize.admin_password :
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Informations d'identification manquantes ou incorrectes")
    response.status_code = status.HTTP_201_CREATED
    quize.admin_username = ""
    quize.admin_password = ""
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

api = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")

api.include_router(unauthenticated_router)
api.include_router(authenticated_router)
