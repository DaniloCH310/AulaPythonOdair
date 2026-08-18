# Design: Atividade de `print` em Python

## Objetivo

Criar uma atividade introdutória em Python que apresente uma jornada de aprendizado por meio de mensagens exibidas no terminal.

## Estrutura

- O programa ficará no arquivo `AtividadePrint.py`.
- O arquivo conterá exatamente 20 chamadas independentes a `print(...)`.
- Cada chamada exibirá uma frase inédita em português.
- As frases formarão uma sequência: primeiros contatos com Python, prática de conceitos básicos e evolução do estudante.
- O programa não terá entradas, dependências externas, funções, listas ou laços.

## Comportamento

Ao executar `python AtividadePrint.py`, o terminal exibirá exatamente 20 linhas não vazias. Todas permanecerão no contexto de aprendizagem e programação em Python, sem reutilizar literalmente as frases fornecidas como referência.

## Validação

- Compilar o arquivo com o módulo `py_compile`.
- Executar o programa com Python.
- Confirmar que a saída contém exatamente 20 linhas não vazias.
- Inspecionar o diff para garantir que somente os arquivos planejados foram alterados.

## Publicação

Como o repositório está vazio, a especificação formará o primeiro commit na branch `main`. Após a aprovação desta especificação, o código será implementado, validado e publicado em commits subsequentes na mesma branch.
