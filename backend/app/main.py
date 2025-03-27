from fastapi import FastAPI
from app.routes import company_routes

app = FastAPI(title="Company API")
app.include_router(company_routes.router)


@app.get("/")
def read_root():
    return {"message": "Olá mundo!"}
