from sqlalchemy.orm import Session
from app.models.company import Company
from sqlalchemy.exc import SQLAlchemyError


def get_companies_by_name(db: Session, name: str):
    try:
        return (
            db.query(Company)
            .filter(Company.nome_fantasia.ilike(f"%{name}%"))
            .order_by(Company.nome_fantasia)
            .all()
        )
    except SQLAlchemyError as e:
        return {"error": str(e)}

def get_all_companies(db: Session):
    try:
        return db.query(Company).all()
    except SQLAlchemyError as e:
        return {"error": str(e)}


def get_by_cnpj(db: Session, cnpj: str):
    try:
        return (
            db.query(Company)
            .filter(Company.cnpj.ilike(f"{cnpj}%")) 
            .all()
        )
    except SQLAlchemyError as e:
        return {"error": str(e)}