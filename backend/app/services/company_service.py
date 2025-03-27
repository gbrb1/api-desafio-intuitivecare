from sqlalchemy.orm import Session
from app.repositories.company_repo import get_companies_by_name, get_all_companies, get_by_cnpj as get_cnpj

def search_companies(db: Session, name: str):
    try:
        return get_companies_by_name(db, name)
    except Exception as e:
        return {"error": str(e)}

def get_all(db: Session):
    try:
        return get_all_companies(db)
    except Exception as e:
        return {"error": str(e)}

def get_by_cnpj(db: Session, cnpj: str):
    try:
        return get_cnpj(db, cnpj)
    except Exception as e:
        return {"error": str(e)}
