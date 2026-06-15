# PLANO DE TESTES — PyTest-ServeRest
 
## Objetivo da Suíte
 
Validar o funcionamento correto da API REST ServeRest por meio de testes automatizados, cobrindo os principais endpoints da aplicação e garantindo que as respostas estejam de acordo com o contrato esperado em cenários de sucesso, de erro e de valores extremos.
 
---
 
## Estratégia
 
- **Tipo de teste:** Testes funcionais (comportamento dos endpoints), não-funcionais (tempo de resposta) e testes negativos/edge cases (entradas inválidas e valores extremos)
- **Camada:** Backend — API REST
- **Ferramentas:**
  - Python 3.14.4 — linguagem base
  - Pytest 9.0.3 — framework de execução dos testes
  - requests — realização das chamadas HTTP
  - time — medição de tempo de resposta e geração de dados únicos
---
 
## Escopo
 
### O que está coberto
 
| Endpoint         | Métodos testados              | Arquivo                  |
|------------------|-------------------------------|--------------------------|
| `/login`         | POST                          | `test_api_user.py`       |
| `/usuarios`      | GET, POST, PUT, DELETE        | `test_api_user.py`       |
| `/produtos`      | GET, POST, PUT, DELETE        | `test_api_prod.py`       |
| `/produtos`      | POST (edge cases)             | `test_api_ext.py`        |
 
### O que ficou fora
 
- Rota `/carrinhos` — escopo não atingido nesta fase
- Testes de interface web (`front.serverest.dev`)
- Testes de carga ou stress (ex: Locust, k6)
- `POST /produtos` com token de não-admin (403) — `aux_func` sempre cria usuário administrador
 
## Cenários a Implementar
 
### `/login`
- [x] POST — login com credenciais válidas retorna token
- [x] POST — login com senha incorreta retorna 401
- [x] POST — login com email não cadastrado retorna 401
- [x] POST — login com body vazio retorna 400
### `/usuarios`
- [x] GET — listar todos os usuários retorna 200 com lista
- [x] GET — buscar usuário por ID válido retorna 200
- [x] GET — buscar usuário por ID inexistente retorna 400
- [x] POST — criar usuário administrador com dados válidos retorna 201
- [x] POST — criar usuário com email já cadastrado retorna 400
- [x] POST — criar usuário sem campo obrigatório retorna 400
- [x] PUT — atualizar usuário existente retorna 200
- [x] PUT — atualizar usuário com ID inexistente cria novo registro (201)
- [x] DELETE — excluir usuário sem carrinho ativo retorna 200
- [x] DELETE — excluir usuário com carrinho ativo retorna 400
- [x] DELETE — excluir usuário com ID inexistente retorna 200 sem exclusão
### `/produtos`
- [x] GET — listar todos os produtos retorna 200 com lista
- [x] GET — buscar produto por ID válido retorna 200
- [x] GET — buscar produto por ID inexistente retorna 400
- [x] POST — criar produto com token de admin retorna 201
- [x] POST — criar produto sem autenticação retorna 401
- [x] POST — criar produto com nome já existente retorna 400
- [x] PUT — atualizar produto com token válido retorna 200
- [x] PUT — atualizar produto com ID inexistente cria novo registro (201)
- [x] DELETE — excluir produto sem carrinho ativo retorna 200
- [x] DELETE — excluir produto com ID inexistente retorna 200 sem exclusão
- [x] DELETE — excluir produto sem token retorna 401
### `/carrinhos`
- [ ] GET — listar todos os carrinhos retorna 200 com lista
- [ ] GET — buscar carrinho por ID válido retorna 200
- [ ] POST — criar carrinho com produtos válidos retorna 201
- [ ] POST — criar segundo carrinho para mesmo usuário retorna 400
- [ ] POST — criar carrinho sem autenticação retorna 401
- [ ] POST — criar carrinho com produto inexistente retorna 400
- [ ] DELETE `/concluir-compra` — conclui compra e reestoca produtos retorna 200
- [ ] DELETE `/cancelar-compra` — cancela compra e reestoca produtos retorna 200
### Edge Cases — `/produtos` (marcados com `@pytest.mark.edge`)
- [x] POST — preço negativo
- [x] POST — preço zero
- [x] POST — preço como string
- [x] POST — quantidade negativa
- [x] POST — quantidade zero
- [x] POST — quantidade como string
- [x] POST — nome vazio
- [x] POST — nome com 10.000 caracteres
- [x] POST — nome com `<script>` (XSS)
- [x] POST — nome com apenas espaços
- [x] POST — sem campo nome
- [x] POST — sem campo preço
- [x] POST — sem campo descrição
- [x] POST — sem campo quantidade
- [x] POST — body vazio
- [x] POST — campo extra no body
- [x] POST — SQL injection no nome
### Não-funcionais
- [x] Tempo de resposta do `POST /login` inferior a 3 segundos
- [x] Tempo de resposta do `POST /produtos` inferior a 3 segundos
- [x] Tempo de resposta do `POST /usuarios` inferior a 3 segundos
---
 
## Critérios de Qualidade
 
Um teste está **pronto** quando:
 
- O nome da função segue o padrão `test_<metodo>_<recurso>_<cenario>` (ex: `test_post_login_credenciais_validas`)
- O status HTTP da resposta é validado com `assert`
- O corpo da resposta é validado nos campos relevantes (ex: presença de `_id`, mensagem de erro esperada)
- Todo recurso criado durante o teste (usuário, produto, carrinho) é removido ao final, via fixture com `yield` e teardown
- O teste é independente — não depende de estado deixado por outro teste
- Testes não-funcionais registram o tempo com `time` e validam o limite definido