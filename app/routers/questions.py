from fastapi import APIRouter, HTTPException, Response, status, HTTPException

from .quizes import Quize

questions_router = APIRouter() 

ADMIN_USER = {
  "admin_username": "admin",
  "admin_password": "un_bon_password"
}

class AdminQuize(Quize):
    admin_username: str
    admin_password: str
 
@questions_router.post('/create_question', name="Creation de nouvel question ")
def create_question(quize: AdminQuize,  response: Response): 
    """Crée une nouvelle question par un utilisateur admin.
    """
    if ADMIN_USER["admin_username"]!=quize.admin_username or ADMIN_USER["admin_password"]!=quize.admin_password :
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Informations d'identification manquantes ou incorrectes")
    response.status_code = status.HTTP_201_CREATED
    
    #TODO : save in DB then return created question  
    quize.admin_username = ""
    quize.admin_password = ""
    
    return quize