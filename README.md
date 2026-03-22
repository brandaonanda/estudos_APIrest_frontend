# 🚀 API REST + Frontend (CRUD de Equipamentos)

Projeto completo de **API REST com FastAPI** + **Frontend em HTML/JavaScript**, permitindo realizar operações de **CRUD (Create, Read, Update, Delete)** em equipamentos.

📚 Este projeto faz parte dos meus estudos autodidatas em tecnologia, com foco em desenvolvimento de APIs, integração de sistemas e construção de bases para aplicações mais avançadas, como monitoramento inteligente, análise de dados e soluções com Inteligência Artificial.

---

## 🌐 🔗 Acesse o projeto online

- 🖥️ **Frontend (Netlify):**  
👉 https://apirest-frontend-study-fernanda.netlify.app/

- ⚙️ **API (Render):**  
👉 https://estudos-apirest-frontend-backend.onrender.com

---

## 🧠 📌 O que esse projeto faz?

Permite gerenciar equipamentos com as seguintes funcionalidades:

✔ Listar todos os equipamentos  
✔ Buscar equipamento por ID  
✔ Criar novo equipamento  
✔ Atualizar equipamento existente  
✔ Deletar equipamento  

---

## 🛠️ Tecnologias utilizadas

### 🔙 Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

### 🌐 Frontend
- HTML5
- JavaScript (Fetch API)

### ☁️ Deploy
- Render (backend)
- Netlify (frontend)

---

## 📡 Endpoints da API

| Método | Endpoint | Descrição |
|--------|--------|----------|
| GET | `/equipamentos` | Lista todos os equipamentos |
| GET | `/equipamentos/{id}` | Busca por ID |
| POST | `/equipamentos` | Cria novo equipamento |
| PUT | `/equipamentos/{id}` | Atualiza equipamento |
| DELETE | `/equipamentos/{id}` | Deleta equipamento |

---

## 📦 Exemplo de JSON

```json
{
  "id": 1,
  "nome": "Motor",
  "status": "ok"
}
