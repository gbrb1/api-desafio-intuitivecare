from sqlalchemy import Column, String, Integer, Date
from app.database import Base

class Company(Base):
    __tablename__ = "empresas"

    registro_ans = Column(String(10), primary_key=True)
    cnpj = Column(String(14), primary_key=True)
    razao_social = Column(String(255), index=True)
    nome_fantasia = Column(String(255), index=True)
    modalidade = Column(String(255))
    logradouro = Column(String(255))
    numero = Column(String(50))
    complemento = Column(String(255))
    bairro = Column(String(255))
    cidade = Column(String(255))
    uf = Column(String(2))
    cep = Column(String(8))
    ddd = Column(String(2))
    telefone = Column(String(20))
    fax = Column(String(20))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(255))
    regiao_de_comercializacao = Column(Integer)
    data_registro_ans = Column(Date)
