from fastapi import APIRouter, HTTPException, Response, status, HTTPException, Depends
from fastapi.responses import JSONResponse 
from pydantic import BaseModel
from typing import Optional, List
import pandas as pd
from dependencies import verify_authorization_header  

quizes_router = APIRouter(
        dependencies=[Depends(verify_authorization_header)],
        responses={404: {"description": "Not found"}},
    )  

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

class QuizeListDescription(BaseModel):
    """Description d'une list de Quiz
    """
    test_type: str
    categories: List[str]
    number_of_questions: int


@quizes_router.post('/generate_quiz', name="Génèration des QCM " )
def generate_quiz(desc: QuizeListDescription ):
    """Génère un QCM basé sur les paramètres fournis.
    Le type de test (test_type) dois etre renseigné.
    Le nombre des question (number_of_questions) doisetre entre 1 et 10 

    """
    if desc.number_of_questions < 1: 
        raise HTTPException(
            status_code=422,
            detail="Le nombre des question doisetre entre 1 et 10"
        )
    if desc.test_type == "": 
        raise HTTPException(
            status_code=422,
            detail="Le type de test (test_type) dois etre renseigné "
        )

    return get_random_questions(desc.number_of_questions, desc.categories, desc.test_type)

 
def get_random_questions(size: int,  categories: List[str], test_type: str ) : 
    '''
    Fonction qui renvois N question selectionneés aléatoirement à partire de la base de donné (le fichier CSV). 
    '''
    # read csv file 
    df = pd.read_csv("../questions.csv")
    
    #filter data 
    df = df.query('use == @test_type and subject in @categories')

    # geta random list
    df = df.sample(n=size) 

    df = df.to_json(orient="records") 
    print(df)

    #json_compatible_item_data = jsonable_encoder(df)
    return JSONResponse(content=df)
    #return df
