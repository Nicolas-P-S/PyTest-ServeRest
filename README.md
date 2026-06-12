# 🧪 PyTest-ServeRest

Suite de testes automatizados para a API [ServeRest](https://compassuol.serverest.dev), desenvolvida com **Python** e **pytest**.

---

## 📋 Sobre o projeto

Este projeto valida os endpoints da API ServeRest, cobrindo os fluxos de **usuários**: cadastro, login, listagem, busca por ID, atualização e remoção. Os testes seguem boas práticas de isolamento — cada teste cria e limpa seus próprios dados, sem depender de estado global.

---

## 🗂️ Estrutura do projeto

```
PyTest-ServeRest/
├── docs/                  # Documentação adicional
├── tests/
│   ├── conftest.py        # Fixtures compartilhadas (user, auth_token)
│   ├── test_api_user.py   # Casos de teste da API de usuários
│   └── aux_func.py        # Funções auxiliares e helpers de requisição
├── .gitignore
└── README.md
```

---

## ✅ Cobertura de testes

### Base
| Teste | Descrição |
|---|---|
| `test_endpoint_call_200` | Verifica se a API está online |

### Usuários — Listagem
| Teste | Descrição |
|---|---|
| `test_list_users_should_return_200` | Lista usuários com sucesso |
| `test_list_users_should_return_quantidade_field` | Valida campo `quantidade` na resposta |
| `test_list_users_quantity_increases_after_register` | Quantidade aumenta ao cadastrar |
| `test_list_users_quantity_decreases_after_delete` | Quantidade diminui ao deletar |

### Usuários — Login
| Teste | Descrição |
|---|---|
| `test_login_valid_user_should_return_200` | Login com credenciais válidas |
| `test_login_invalid_user_should_return_401` | Login com credenciais inválidas |
| `test_login_without_email_should_return_400` | Login sem email retorna 400 |
| `test_login_without_password_should_return_400` | Login sem senha retorna 400 |
| `test_login_returns_bearer_token_format` | Token retornado no formato `Bearer <token>` |

### Usuários — Cadastro
| Teste | Descrição |
|---|---|
| `test_register_valid_user_should_return_201` | Cadastro com dados válidos |
| `test_register_duplicate_user_should_return_400` | Cadastro duplicado retorna 400 |
| `test_register_without_email_should_return_400` | Cadastro sem email retorna 400 |
| `test_register_without_name_should_return_400` | Cadastro sem nome retorna 400 |
| `test_register_without_password_should_return_400` | Cadastro sem senha retorna 400 |
| `test_register_with_invalid_email_format_should_return_400` | Email inválido retorna 400 |
| `test_register_user_fields_are_persisted` | Campos persistidos; senha não exposta |

### Usuários — Busca por ID
| Teste | Descrição |
|---|---|
| `test_get_user_by_valid_id_should_return_200` | Busca usuário existente |
| `test_get_user_by_invalid_id_should_return_400` | Busca com ID inválido retorna 400 |
| `test_get_user_returns_correct_fields` | Resposta contém todos os campos esperados |
| `test_get_user_id_matches_requested` | ID retornado corresponde ao solicitado |

### Usuários — Atualização
| Teste | Descrição |
|---|---|
| `test_update_user_should_return_200` | Atualização com dados válidos |
| `test_update_user_name_should_persist` | Nome atualizado é persistido |
| `test_update_user_without_name_should_return_400` | Atualização sem nome retorna 400 |
| `test_update_user_with_duplicate_email_should_return_400` | Email já em uso retorna 400 |
| `test_update_invalid_user_should_return_400` | ID inválido retorna 400 |

### Usuários — Remoção
| Teste | Descrição |
|---|---|
| `test_delete_user_should_return_200` | Remoção de usuário existente |
| `test_delete_user_should_not_be_found_after_deletion` | Usuário não encontrado após deleção |
| `test_delete_same_user_twice_should_return_200_then_200` | Dupla deleção retorna 200 nos dois casos |
| `test_delete_invalid_user_should_return_400` | ID inválido retorna 200 (comportamento da API) |

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Nicolas-P-S/PyTest-ServeRest.git
cd PyTest-ServeRest

# Instale as dependências
pip install pytest requests
```

### Executando os testes

```bash
# Todos os testes
pytest

# Com output detalhado
pytest -v

# Um teste específico
pytest tests/test_api_user.py::test_register_valid_user_should_return_201 -v

# Com relatório de tempo de execução
pytest -v --durations=10
```

---

## 🔧 Detalhes de implementação

### Geração de emails únicos

Cada chamada a `register()` gera um email único via timestamp em milissegundos, evitando conflitos entre testes executados em sequência:

```python
def generate_email():
    return f"test_{int(time.time() * 1000)}@qa.com"
```

### Fixtures com teardown automático

A fixture `user` cria um usuário antes do teste e o remove automaticamente ao final, mantendo o ambiente limpo:

```python
@pytest.fixture
def user():
    response = register()
    user_id = response.json()["_id"]
    yield user_id
    delete_user(user_id)  # teardown automático
```

### Email rastreável na resposta

A função `register()` anexa o email utilizado diretamente no objeto de resposta, facilitando o reuso sem variáveis globais:

```python
response.used_email = email
```

---

## 🌐 API utilizada

**ServeRest** — API REST pública para prática de testes.

| Info | Valor |
|---|---|
| Base URL | `https://compassuol.serverest.dev` |
| Documentação | [https://serverest.dev](https://serverest.dev) |
| Autenticação | Bearer Token (JWT) |

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/)
- [Requests](https://requests.readthedocs.io/)
- [ServeRest API](https://serverest.dev)

---

## 👤 Autor

**Nicolas P. S.**
[github.com/Nicolas-P-S](https://github.com/Nicolas-P-S)