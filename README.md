# quiz_api (with FastAPI)
Quiz API  

# Instalation

Installer de l'envirenement avec la commande :
```bash
pip install --no-cache-dir --upgrade -r requirements.txt
```

Lancer le surveur [uvicorn](https://www.uvicorn.org/)  vec la commande :

```bash
uvicorn main:api --reload
```
Se placer dans le dossier _app_ et lancer les tests  [PyTest](https://docs.pytest.org) avec la commande :

```bash
python -m pytest tests
```

# Architecture de l'application:

/
├── app
│   ├── main.py
│   ├── dependencies.py
│   ├── routers
│   │   ├── questions.py
│   │   └── quizes.py
│   └── tests
│       ├── main_test.py
│       └── routers
│           ├── questions_test.py
│           └── quizes_test.py
├── requirements.txt
├── ...
└── ...