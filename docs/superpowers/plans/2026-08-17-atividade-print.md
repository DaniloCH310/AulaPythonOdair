# Atividade de `print` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar e publicar um programa introdutório que exiba uma jornada de aprendizado de Python em exatamente 20 chamadas independentes a `print(...)`.

**Architecture:** Um único script sequencial, sem entradas, funções, coleções, laços ou dependências externas. Cada instrução `print(...)` produz uma linha da narrativa, e a validação usa o próprio interpretador Python e a contagem da saída no PowerShell.

**Tech Stack:** Python 3, PowerShell e Git.

**Spec:** `docs/superpowers/specs/2026-08-17-atividade-print-design.md`

## Global Constraints

- O programa deve ficar em `AtividadePrint.py`.
- O arquivo deve conter exatamente 20 chamadas independentes a `print(...)`.
- Cada chamada deve exibir uma frase inédita em português.
- As frases devem formar uma jornada de aprendizado de Python.
- Não adicionar entradas, dependências externas, funções, listas ou laços.
- A execução deve produzir exatamente 20 linhas não vazias.

---

### Task 1: Criar e validar o programa

**Files:**
- Create: `AtividadePrint.py`

**Interfaces:**
- Consumes: interpretador Python 3 disponível como `python`.
- Produces: processo de terminal com exatamente 20 linhas não vazias em `stdout` e código de saída zero.

- [ ] **Step 1: Demonstrar que o comportamento ainda não existe**

Run: `python AtividadePrint.py`

Expected: FAIL com mensagem equivalente a `can't open file`, pois o script ainda não existe.

- [ ] **Step 2: Criar a implementação mínima**

Criar `AtividadePrint.py` com o conteúdo exato:

```python
print("Hoje dei mais um passo na minha jornada com Python.")
print("Comecei explorando como o comando print exibe informações.")
print("Cada linha executada torna a sintaxe mais familiar.")
print("Estou descobrindo como o Python interpreta minhas instruções.")
print("As mensagens no terminal mostram o resultado do meu código.")
print("Com prática, os comandos deixam de parecer complicados.")
print("Os erros também ensinam onde posso melhorar.")
print("A atenção aos detalhes faz diferença ao programar.")
print("Estou fortalecendo minha lógica a cada atividade.")
print("Python permite transformar ideias em soluções.")
print("Novos exercícios ampliam minha experiência com a linguagem.")
print("Organizar o código facilita a leitura e a manutenção.")
print("A curiosidade me ajuda a testar possibilidades diferentes.")
print("Entender a sintaxe é parte importante do aprendizado.")
print("Pequenos programas preparam o caminho para projetos maiores.")
print("Continuar praticando aumenta minha confiança.")
print("Já consigo acompanhar melhor a execução do programa.")
print("Meu progresso aparece em cada desafio concluído.")
print("Ainda há muito para aprender no universo do Python.")
print("Esta atividade marca mais uma conquista na programação.")
```

- [ ] **Step 3: Validar a sintaxe**

Run: `python -m py_compile AtividadePrint.py`

Expected: PASS, sem saída e com código de saída zero.

- [ ] **Step 4: Validar o comportamento observável**

Run:

```powershell
$output = @(python AtividadePrint.py)
if ($LASTEXITCODE -ne 0) { throw "O programa falhou com código $LASTEXITCODE" }
if ($output.Count -ne 20) { throw "Esperadas 20 linhas; obtidas $($output.Count)" }
if (@($output | Where-Object { [string]::IsNullOrWhiteSpace($_) }).Count -ne 0) { throw "A saída contém linha vazia" }
$output
```

Expected: PASS com 20 frases não vazias e código de saída zero.

- [ ] **Step 5: Inspecionar e registrar a implementação**

Run:

```powershell
git diff --check
rg -c '^print\(' AtividadePrint.py
git status -sb
git add -- AtividadePrint.py
git commit -m "adiciona atividade de prints"
```

Expected: `git diff --check` sem erros, `rg` retornando `20` e commit contendo somente `AtividadePrint.py` além dos commits anteriores de documentação.

### Task 2: Publicar e conferir o repositório

**Files:**
- No file changes.

**Interfaces:**
- Consumes: branch local `main`, remoto `origin` e autenticação GitHub existente.
- Produces: branch `main` publicada em `DaniloCH310/AulaPythonOdair` com todo o histórico local.

- [ ] **Step 1: Confirmar escopo antes do envio**

Run:

```powershell
git status -sb
git log --oneline --decorate -5
git remote -v
```

Expected: árvore limpa, branch `main` e `origin` apontando para `https://github.com/DaniloCH310/AulaPythonOdair.git`.

- [ ] **Step 2: Enviar a branch inicial**

Run: `git push -u origin main`

Expected: criação bem-sucedida de `origin/main`.

- [ ] **Step 3: Verificar a publicação**

Run:

```powershell
gh repo view DaniloCH310/AulaPythonOdair --json defaultBranchRef,url
gh api repos/DaniloCH310/AulaPythonOdair/contents/AtividadePrint.py --jq '.name + " " + .sha'
```

Expected: branch padrão `main`, URL correta e `AtividadePrint.py` encontrado no GitHub.
