# PLANO DE TESTES — PyTest-ServeRest
 
## Objetivo da Suíte
 
Validar o funcionamento correto da API REST ServeRest por meio de testes automatizados, cobrindo os principais endpoints da aplicação e garantindo que as respostas estejam de acordo com o contrato esperado em cenários de sucesso e de erro.
 
---
 
## Estratégia
 
- **Tipo de teste:** Testes funcionais (comportamento dos endpoints) e não-funcionais (tempo de resposta)
- **Camada:** Backend — API REST
- **Ferramentas:**
  - Python 3.14.4 — linguagem base
  - Pytest 9.0.3 — framework de execução dos testes
  - requests — realização das chamadas HTTP
  - time — medição de tempo de resposta
---
 
## Escopo
 
### O que está coberto
 
| Endpoint         | Métodos testados              |
|------------------|-------------------------------|
| `/login`         | POST                          |
| `/usuarios`      | GET, POST, PUT, DELETE        |
| `/produtos`      | GET, POST, PUT, DELETE        |
| `/carrinhos`     | GET, POST, DELETE             |
 
### O que ficou fora
 
- Testes de interface web (`front.serverest.dev`)
- Testes de carga ou stress (ex: Locust, k6)
- Testes de segurança / autenticação avançada (ex: OWASP)
---
 
## Cenários a Implementar
 
### `/login`
- [ ] POST — login com credenciais válidas retorna token
- [ ] POST — login com senha incorreta retorna 401
- [ ] POST — login com email não cadastrado retorna 401
- [ ] POST — login com body vazio retorna 400
### `/usuarios`
- [ ] GET — listar todos os usuários retorna 200 com lista
- [ ] GET — buscar usuário por ID válido retorna 200
- [ ] GET — buscar usuário por ID inexistente retorna 400
- [ ] POST — criar usuário administrador com dados válidos retorna 201
- [ ] POST — criar usuário com email já cadastrado retorna 400
- [ ] POST — criar usuário sem campo obrigatório retorna 400
- [ ] PUT — atualizar usuário existente retorna 200
- [ ] PUT — atualizar usuário com ID inexistente cria novo registro (201)
- [ ] DELETE — excluir usuário sem carrinho ativo retorna 200
- [ ] DELETE — excluir usuário com carrinho ativo retorna 400
- [ ] DELETE — excluir usuário com ID inexistente retorna 200 sem exclusão
### `/produtos`
- [ ] GET — listar todos os produtos retorna 200 com lista
- [ ] GET — buscar produto por ID válido retorna 200
- [ ] GET — buscar produto por ID inexistente retorna 400
- [ ] POST — criar produto com token de admin retorna 201
- [ ] POST — criar produto sem autenticação retorna 401
- [ ] POST — criar produto com token de não-admin retorna 403
- [ ] POST — criar produto com nome já existente retorna 400
- [ ] PUT — atualizar produto com token válido retorna 200
- [ ] DELETE — excluir produto sem carrinho ativo retorna 200
- [ ] DELETE — excluir produto em carrinho ativo retorna 400
- [ ] DELETE — excluir produto com ID inexistente retorna 200 sem exclusão
### `/carrinhos`
- [ ] GET — listar todos os carrinhos retorna 200 com lista
- [ ] GET — buscar carrinho por ID válido retorna 200
- [ ] POST — criar carrinho com produtos válidos retorna 201
- [ ] POST — criar segundo carrinho para mesmo usuário retorna 400
- [ ] POST — criar carrinho sem autenticação retorna 401
- [ ] POST — criar carrinho com produto inexistente retorna 400
- [ ] POST — criar carrinho com quantidade acima do estoque retorna 400
- [ ] DELETE `/concluir-compra` — conclui compra e reestoca produtos retorna 200
- [ ] DELETE `/cancelar-compra` — cancela compra e reestoca produtos retorna 200
### Não-funcionais
- [ ] Tempo de resposta do `POST /login` inferior a 3 segundos
- [ ] Tempo de resposta do `GET /usuarios` inferior a 3 segundos
- [ ] Tempo de resposta do `GET /produtos` inferior a 3 segundos
---
 
## Critérios de Qualidade
 
Um teste está **pronto** quando:
 
- O nome da função segue o padrão `test_<metodo>_<recurso>_<cenario>` (ex: `test_post_login_credenciais_validas`)
- O status HTTP da resposta é validado com `assert`
- O corpo da resposta é validado nos campos relevantes (ex: presença de `_id`, mensagem de erro esperada)
- Todo recurso criado durante o teste (usuário, produto, carrinho) é removido ao final, via fixture com `yield` e teardown
- O teste é independente — não depende de estado deixado por outro teste
- Testes não-funcionais registram o tempo com `time` e validam o limite definido