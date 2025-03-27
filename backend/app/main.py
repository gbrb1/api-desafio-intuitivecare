from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import company_routes

app = FastAPI(title="Company API")

# Configuração de CORS
origins = [
    "*",  # Isso permite todas as origens. Caso queira restringir, substitua "*" por uma lista de URLs.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Registrar as rotas
app.include_router(company_routes.router)

@app.get("/")
def read_root():
    return {"message": "Olá mundo!"}
