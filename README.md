# 📝 API de Gerenciamento de Tarefas

Esta é uma API para gerenciamento de tarefas que permite criar, listar, atualizar e deletar tarefas. A API foi desenvolvida utilizando **Python** e o framework **Flask**, proporcionando uma estrutura leve e eficiente para o gerenciamento de tarefas.

## ⚙️ Funcionalidades

- 📝 **Criar** uma nova tarefa com título e descrição.
- 📋 **Listar** todas as tarefas registradas.
- 🔍 **Listar tarefa específica** pelo ID.
- ✏️ **Atualizar** tarefas existentes (título, descrição, status de conclusão).
- ❌ **Deletar** tarefas específicas.
- ✅ **Testes** automatizados utilizando **pytest**.
- 📑 **Documentação** interativa com **Swagger**.

## 🛠️ Tecnologias Utilizadas

- **🐍 Python**: Linguagem de programação.
- **🌐 Flask**: Framework web utilizado para construir a API.
- **🗄️ SQLite**: Banco de dados utilizado para armazenar as tarefas.
- **🧪 Pytest**: Framework utilizado para escrever e executar testes automatizados.
- **📖 Swagger**: Utilizado para documentação da API.

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/joschonarth/flask-task-manager
    ```
   
2. Acesse o diretório do projeto:
    ```bash
    cd flask-task-manager
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```bash
    flask run
    ```

5. A API estará disponível em: `http://127.0.0.1:5000`

## 🧪 Como Rodar os Testes

Para rodar todos os testes, no modo detalhado (`-v`), execute o seguinte comando:

```bash
pytest tests.py -v
```

## 🔗 Servidor de Desenvolvimento

- **URL**: `http://127.0.0.1:5000`

## 📋 Endpoints

### 1. 📋 Obter todas as tarefas
- **Método**: **`GET`** `/tasks`
- **Descrição**: Retorna a lista de todas as tarefas.
- **Resposta**:
    - `200 OK`: Retorna a lista de tarefas com os campos `id`, `title`, `description`, `completed` e o total de tarefas (`total_tasks`).

### 2. 🔍 Obter tarefa específica
- **Método**: **`GET`** `/tasks/{taskId}`
- **Descrição**: Retorna uma tarefa específica com base no ID fornecido.
- **Parâmetros**:
    - `taskId`: ID da tarefa a ser retornada (passado na URL).
- **Resposta**:
    - `200 OK`: Retorna os dados da tarefa encontrada.

### 3. 📝 Criar nova tarefa
- **Método**: **`POST`** `/tasks`
- **Descrição**: Cria uma nova tarefa.
- **Corpo da Requisição**:
    ```json
    {
      "title": "Título da tarefa",
      "description": "Descrição da tarefa"
    }
    ```
- **Resposta**:
    - `200 OK`: Retorna os dados da nova tarefa criada.

### 4. ✏️ Atualizar tarefa existente
- **Método**: **`PUT`** `/tasks/{taskId}`
- **Descrição**: Atualiza os dados de uma tarefa existente.
- **Parâmetros**:
    - `taskId`: ID da tarefa a ser atualizada (passado na URL).
- **Corpo da Requisição**:
    ```json
    {
      "title": "Novo título da tarefa",
      "description": "Nova descrição da tarefa",
      "completed": true
    }
    ```
- **Resposta**:
    - `200 OK`: Tarefa atualizada com sucesso.

### 5. ✅ Marcar ou desmarcar tarefa
- **Método**: **`PATCH`** `/tasks/{taskId}/complete`
- **Descrição**: Marca ou desmarca uma tarefa como concluída.
- **Parâmetros**:
    - `taskId`: ID da tarefa a ser marcada ou desmarcada (passado na URL).
- **Resposta**:
    - `200 OK`: Retorna uma mensagem confirmando a alteração do status da tarefa.
    - `404 Not Found`: Mensagem de erro caso a tarefa não seja encontrada.

### 6. ❌ Deletar tarefa
- **Método**: **`DELETE`** `/tasks/{taskId}`
- **Descrição**: Deleta uma tarefa existente.
- **Parâmetros**:
    - `taskId`: ID da tarefa a ser deletada (passado na URL).
- **Resposta**:
    - `200 OK`: Tarefa deletada com sucesso.


## 📚 Documentação

A documentação da API está disponível no Swagger no arquivo: [openapi.x-yaml](./openapi.x-yaml)


## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver ideias para melhorias ou correções, faça um fork deste repositório, crie uma branch com suas alterações e envie um pull request.


## 📞 Contato 

<div>
    <a href="https://www.linkedin.com/in/joschonarth/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:joschonarth@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>