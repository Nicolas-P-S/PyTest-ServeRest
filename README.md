# PyTest-ServeRest

Suíte de testes automatizados para a API REST [ServeRest](https://serverest.dev), desenvolvida com Python e Pytest.

---

## 🛠️ Tecnologias

- Python 3.14.4
- Pytest 9.0.3
- requests
- time

---

## 📁 Estrutura

```
PyTest-ServeRest/
├── tests/
│   ├── test_api_user.py       # Testes da rota /usuarios
│   ├── test_api_prod.py       # Testes da rota /produtos
│   ├── test_api_ext.py        # Edge cases e testes negativos
│   ├──aux_func.py             # Funções auxiliares e helpers
│   └──conftest.py             # Fixtures globais
├── pytest.ini                 # Configuração de markers
├── PLANO-DE-TESTES.md
└── README.md
```

---

## ▶️ Como executar

```bash
# Instalar dependências
pip install pytest requests

# Rodar todos os testes (exceto edge cases)
Linux: pytest tests/ -v -m "not edge"
Windows: python -m pytest tests/ -v -m "not edge"

# Rodar apenas edge cases
Linux: pytest tests/ -v -m edge
Windows: python -m pytest tests/ -v -m edge

# Rodar tudo
Linux: pytest tests/ -v
Windows: python -m pytest tests/ -v
```

---

## 📊 Cobertura de Testes

Método de cálculo baseado no artigo [Como verificar a cobertura de testes da API REST](https://medium.com/revista-dtar/como-verificar-a-cobertura-de-testes-da-api-rest-9e2f745564b), utilizando dois critérios:

### 1. Operator Coverage — cobertura por operações (método + endpoint)

Mede quantas combinações de método HTTP + endpoint foram testadas em relação ao total disponível na API.

| Endpoint              | GET | POST | PUT | DELETE |
|-----------------------|-----|------|-----|--------|
| `/login`              | —   | ✅   | —   | —      |
| `/usuarios`           | ✅  | ✅   | ✅  | ✅     |
| `/produtos`           | ✅  | ✅   | ✅  | ✅     |
| `/carrinhos`          | —   | —    | —   | —      |

**Operações testadas: 9 / 13 totais = 69%**

> Carrinhos ficou fora do escopo desta fase — será coberto na próxima iteração.

---

### 2. Cobertura por Cenários

Mede quantos cenários planejados no `PLANO-DE-TESTES.md` foram implementados.

| Módulo      | Planejados | Implementados | Cobertura |
|-------------|------------|---------------|-----------|
| Login       | 4          | 4             | 100%      |
| Usuários    | 15         | 15            | 100%      |
| Produtos    | 11         | 11            | 100%      |
| Carrinhos   | 8          | 0             | 0%        |
| **Total**   | **38**     | **30**        | **79%**   |

---

### O que ficou fora e por quê

| Cenário                          | Motivo                                                  |
|----------------------------------|---------------------------------------------------------|
| Rota `/carrinhos` completa       | Escopo não atingido nesta fase do projeto               |
| `POST /produtos` com token não-admin (403) | `aux_func` sempre registra usuário como administrador |
| `GET /usuarios` com filtro por query param | Não implementado — baixa prioridade             |

---

## 🐛 Bugs Encontrados

Durante a execução dos edge cases (`test_api_ext.py`), foram identificados os seguintes comportamentos inesperados na API:

| Cenário                          | Esperado | Obtido | Severidade |
|----------------------------------|----------|--------|------------|
| `POST /produtos` com quantidade zero | 400  | 201    | Média      |
| `POST /produtos` com nome de 10.000 chars | 400 | 201 | Baixa    |
| `POST /produtos` com `<script>` no nome | 400 | 201  | Alta       |
| `POST /produtos` com nome só de espaços | 400 | 201  | Baixa      |
| `POST /produtos` com SQL injection no nome | 400 | 201 | Alta      |
| `POST /produtos` com campo extra no body | 201 | 400  | Média      |

> Bugs reportados na aba [Issues](https://github.com/Nicolas-P-S/PyTest-ServeRest/issues) do repositório.