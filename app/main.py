from fastapi import FastAPI
from routers.questions import questions_router
from routers.quizes import quizes_router

api = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")

api.include_router(quizes_router)
api.include_router(questions_router)

verify_msg_key="message"
verify_msg="L'API est fonctionnelle"
 
@api.get('/verify', name="Verification de l'API")
def get_verify():
    """Vérifie que l'API est fonctionnelle
    """
    return {
       verify_msg_key : verify_msg
    }