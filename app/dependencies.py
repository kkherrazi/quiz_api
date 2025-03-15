from fastapi import Header, HTTPException
import base64

# USERS DB 
USERS_DB = {
  "khalid": "kherrazi",  #     ->  a2hhbGlkOmtoZXJyYXpp
  "bob": "builder",       
  "alice": "wonderland",
  "clementine": "mandarine"  
}

async def verify_authorization_header(Authorization: str = Header()):
    token = Authorization.replace("Basic ","")
    token = b64encode_decode(token)
    login_password=token.split(":")

    if len(login_password) != 2 or not USERS_DB.get(login_password[0]) or USERS_DB.get(login_password[0]) != login_password[1]:
        raise HTTPException(
            status_code=401,
            detail="Informations d'identification manquantes ou incorrectes",
            headers={"WWW-Authenticate": "Basic"},
        )

def b64encode_encode(login: str,  password: str) : 
    token = base64.b64encode((login + ':' + password).encode('utf-8')).decode('utf-8')
    print(token)
    return token   

def b64encode_decode(token: str) : 
    login_password = base64.b64decode(token).decode('utf-8')
    print(token)
    return login_password   