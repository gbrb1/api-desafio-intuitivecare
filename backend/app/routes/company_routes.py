from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.company_service import search_companies, get_all as get_all_companies, get_by_cnpj

router = APIRouter(prefix="/companies/api", tags=["Companies"])

@router.get("/search")
def search(name: str, db: Session = Depends(get_db)):
    """
    Endpoint para buscar as empresas pelo nome, para utilizar no browser, coloque
    o parâmetro 'name' no final, exemplo:
    http://127.0.0.1:8000/companies/api/search?name=AMERON
    """
    return search_companies(db, name)


@router.get("/getall")
def get_all(db: Session = Depends(get_db)):
    """
    Apenas um getall, para buscar todas as empresas em banco,
    acesse em companies/api/getall, sem parâmetros
    """
    return get_all_companies(db)

@router.get("/getbycnpj")
def get_cnpj(cnpj: str, db: Session = Depends(get_db)):
    """
    Endpoint para buscar as empresas pelo CNPJ, para utilizar no browser, coloque
    o parâmetro 'cnpj' no final, exemplo:
    http://127.0.0.1:8000/companies/api/getbycnpj?cnpj=84638345000165
    """
    return get_by_cnpj(db, cnpj)
