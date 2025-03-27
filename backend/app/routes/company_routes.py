from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.company_service import search_companies, get_all as get_all_companies, get_by_cnpj

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.get("/search")
def search(name: str, db: Session = Depends(get_db)):
    return search_companies(db, name)


@router.get("/getall")
def get_all(db: Session = Depends(get_db)):
    return get_all_companies(db)

@router.get("/getbycnpj")
def get_cnpj(cnpj: str, db: Session = Depends(get_db)):
    return get_by_cnpj(db, cnpj)
