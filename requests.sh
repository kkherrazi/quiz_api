## -------------------------------------------
#  Utilisateurs connus :
#      a2hhbGlkOmtoZXJyYXpp
#      Ym9iOmJ1aWxkZXI=
#      Y2xlbWVudGluZTptYW5kYXJpbmU=
#


## -------------------------------------------
## 1. EndPoint /verify 


# 1. Requête 
# Reponse : HTTP 200 et un message "L'API est fonctionnelle"
curl -X GET http://127.0.0.1:8000/verify


## -------------------------------------------
## 2. EndPoint /generate_quiz 

# Requête 2/1  
# login:password => test:test  N'EST PAS dans la liste des utilisateur connu.
# Reponse : HTTP 401 "Informations d'identification manquantes ou incorrectes" 
#
curl -X 'POST' -i \
  'http://127.0.0.1:8000/generate_quiz' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic dGVzdDp0ZXN0 ' \
  -d '{
      "test_type": "Test de validation",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 4
   }'

# Requête 2/2 
# Login:Password => khalid:kherrazi, utilisateur bien coonu.
# Reponse :  HTTP 200  et un JON contenant 4 questons  
#
curl -X 'POST' -i \
  'http://127.0.0.1:8000/generate_quiz' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic a2hhbGlkOmtoZXJyYXpp' \
  -d '{
      "test_type": "",
      "categories": ["Automation", "Classification"],
      "number_of_questions": 4
   }'


## -------------------------------------------
## 3. EndPoint /create_question   

# Requête 3/1 
# Reponse : HTTP 401 parceque le password ADMIN n'est pas bon.   
curl -X 'POST' -i \
  'http://127.0.0.1:8000/create_question' \
  -H 'Content-Type: application/json' \
  -d '{
    "admin_username": "admin",
    "admin_password": "faux_password",
    "question": "Quelle est la capitale de la France ?",
    "subject": "geography",
    "correct": ["Paris"],
    "use": "multiple_choice",
    "responseA": "Londres",
    "responseB": "Paris",
    "responseC": "Berlin",
    "responseD": "Madrid"
  }'

# Requête 3/2      
# Requête 2 : HTTP 201 et la Qoestion nouvelement créée.   
curl -X 'POST' -i \
  'http://127.0.0.1:8000/create_question' \
  -H 'Content-Type: application/json' \
  -d '{
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
  }'

 
