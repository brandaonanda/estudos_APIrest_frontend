from fastapi import FastAPI  # importa a biblioteca principal do FastAPI

from fastapi.middleware.cors import CORSMiddleware  # importa o middleware de CORS (permite comunicação com frontend)

from pydantic import BaseModel  # importa classe para definir estrutura dos dados (modelo)

app = FastAPI()  # cria a aplicação FastAPI

# configura o CORS para permitir requisições de qualquer origem (frontend)
app.add_middleware(
    CORSMiddleware,  # tipo de middleware
    allow_origins=["*"],  # permite qualquer origem (localhost, etc.)
    allow_credentials=True,  # permite envio de credenciais
    allow_methods=["*"],  # permite todos os métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # permite todos os headers
)

# lista simulando um banco de dados em memória
dados = [
    {"id": 1, "nome": "Motor", "status": "ok"},  # primeiro equipamento
    {"id": 2, "nome": "Bomba", "status": "falha"}  # segundo equipamento
]

# define o modelo de dados esperado nas requisições (estrutura do JSON)
class Equipamento(BaseModel):  # cria uma classe modelo
    id: int  # campo id do tipo inteiro
    nome: str  # campo nome do tipo texto
    status: str  # campo status do tipo texto

# rota básica para testar se API está funcionando
@app.get("/")  # define endpoint raiz "/"
def home():  # função chamada ao acessar a rota
    return {"mensagem": "API funcionando!"}  # retorna um JSON simples

# rota para listar todos os equipamentos
@app.get("/equipamentos")  # endpoint para listar todos
def listar():  # função chamada ao acessar a rota
    return dados  # retorna a lista completa

# rota para buscar equipamento por ID
@app.get("/equipamentos/{id}")  # endpoint com parâmetro (id)
def buscar_por_id(id: int):  # recebe o id como inteiro
    for item in dados:  # percorre todos os dados
        if item["id"] == id:  # verifica se o id bate
            return item  # retorna o item encontrado
    return {"erro": "Equipamento não encontrado"}  # retorna erro se não achar

# rota para criar novo equipamento
@app.post("/equipamentos")  # endpoint POST
def criar(equipamento: Equipamento):  # recebe dados no formato do modelo
    dados.append(equipamento.model_dump())  # adiciona o novo item na lista
    return {"mensagem": "criado"}  # retorna confirmação

# rota para atualizar um equipamento existente
@app.put("/equipamentos/{id}")  # endpoint PUT com id
def atualizar(id: int, equipamento: Equipamento):  # recebe id e novos dados
    for i, item in enumerate(dados):  # percorre lista com índice
        if item["id"] == id:  # se encontrar o id
            dados[i] = equipamento.model_dump()  # substitui pelos novos dados
            return {"mensagem": "atualizado"}  # retorna confirmação
    return {"erro": "Equipamento não encontrado"}  # erro se não achar

# rota para deletar um equipamento
@app.delete("/equipamentos/{id}")  # endpoint DELETE com id
def deletar(id: int):  # recebe id
    for i, item in enumerate(dados):  # percorre lista com índice
        if item["id"] == id:  # se encontrar o item
            del dados[i]  # remove da lista
            return {"mensagem": "deletado"}  # retorna confirmação
    return {"erro": "Equipamento não encontrado"}  # erro se não achar

#CONECTANDO COM FRONT-END (WEB) - arquivo: index.html


#NO TERMINAL: uvicorn API_REST:app --reload
#NA BASH: python -m http.server 5500
#ABRIR NO NAVEGADOR: http://localhost:5500