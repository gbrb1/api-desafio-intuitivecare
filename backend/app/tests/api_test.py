from fastapi.testclient import TestClient
from app.main import app

# mock do banco de dados 
mock_companies = [
    {
        "registro_ans": "1234567890",
        "cnpj": "12345678000195",
        "razao_social": "Empresa Teste 1",
        "nome_fantasia": "Teste1",
        "modalidade": "Saúde",
        "logradouro": "Rua Teste",
        "numero": "123",
        "complemento": "Apt 101",
        "bairro": "Bairro Teste",
        "cidade": "Cidade Teste",
        "uf": "SP",
        "cep": "12345678",
        "ddd": "11",
        "telefone": "1123456789",
        "fax": "1123456789",
        "endereco_eletronico": "contato@empresa1.com",
        "representante": "João da Silva",
        "cargo_representante": "Diretor",
        "regiao_de_comercializacao": 1,
        "data_registro_ans": "2023-01-01"
    },
    {
        "registro_ans": "2345678901",
        "cnpj": "98765432000100",
        "razao_social": "Empresa Teste 2",
        "nome_fantasia": "Teste2",
        "modalidade": "Odontologia",
        "logradouro": "Avenida Teste",
        "numero": "456",
        "complemento": "Bloco B",
        "bairro": "Bairro Teste 2",
        "cidade": "Cidade Teste 2",
        "uf": "RJ",
        "cep": "98765432",
        "ddd": "21",
        "telefone": "2134567890",
        "fax": "2134567890",
        "endereco_eletronico": "contato@empresa2.com",
        "representante": "Maria Oliveira",
        "cargo_representante": "CEO",
        "regiao_de_comercializacao": 2,
        "data_registro_ans": "2023-02-01"
    }
]

# mockando o retorno da função que consulta o banco
def mock_get_company_by_cnpj(cnpj: str):
    return next((company for company in mock_companies if company["cnpj"] == cnpj), None)

# Substituindo a função de consulta no FastAPI com o mock
app.dependency_overrides[mock_get_company_by_cnpj] = mock_get_company_by_cnpj

client = TestClient(app)  

def test_get_all_companies():
    # retorno da lista de empresas
    response = client.get("/companies/api/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 

def test_search_company_by_name():
    response = client.get("/companies/api/search", params={"name": "Teste"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)  

def test_search_company_by_cnpj():
    test_cnpj = "12345678000195"  # CNPJ mockado acima
    response = client.get(f"/companies/api/getbycnpj?cnpj={test_cnpj}")
    
    assert response.status_code == 200
    json_response = response.json()
    
    if json_response:  
        assert isinstance(json_response, dict)  
        assert json_response.get("cnpj") == test_cnpj  
    else:
        assert json_response == []  
