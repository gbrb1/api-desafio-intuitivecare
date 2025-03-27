## <p style="text-align:center;">Tela Inicial</p>
![Tela Inicial](https://i.imgur.com/Ex0namq.png)
<br />
<br />

## <p style="text-align:center;">Busca por nome</p>
![Busca por nome](https://i.imgur.com/4Dtp07t.png)
<br />
<br />

## <p style="text-align:center;">Busca por CNPJ</p>
![Busca por CNPJ](https://i.imgur.com/HmBri7m.png)
<br />
<br />

## <p style="text-align:center;">Exibir todas as empresas</p>
![Todas as empresas](https://i.imgur.com/YqzEOZW.png)
<br />
<br />


# 🚀 Como Rodar o Backend  

## Pré-requisitos  
- Python 3.9+ instalado  
- Pip atualizado (`python -m pip install --upgrade pip`)  
- PostgreSQL 14+ instalado

## Passo a Passo  
Entre na pasta do backend:  
```bash
cd backend/

```

Instale as dependências:
```
pip install -r requirements.txt
```

Configure o banco de dados (arquivo .env na pasta backend):
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_banco  
```
Faça a criação das migrations com o alembic
```
pip install alembic;

alembic init alembic;

from app.database import Base
target_metadata = Base.metadata;


alembic revision --autogenerate -m "Criando tabela empresas"

alembic upgrade head
```

Endpoints Disponíveis

```
GET /companies/api/search?name=termo - Busca por nome
GET /companies/api/getbycnpj?cnpj=123 - Busca por CNPJ
GET /companies/api/getall - Lista todas empresas
```

# 🖥️️ Como Rodar o Frontend
## Pré-requisitos
- Node.js 16+ instalado
- NPM ou Yarn


Entre na pasta frontend:
```
cd frontend/
```


Instale as dependências:
```
npm install
```
Inicie o servidor
```
npm run serve
```

## 🚦 O frontend estará rodando em:
👉 http://localhost:8080

