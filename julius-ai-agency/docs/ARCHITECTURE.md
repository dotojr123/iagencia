# Jules v1.0 - Arquitetura de Agência de IA Autônoma

**Data:** Dezembro de 2025
**Status:** Planejamento & Implementação Inicial
**Versão:** 1.0.0

---

## 1. Visão Geral

Jules v1.0 é uma agência de Inteligência Artificial autônoma projetada para operar com múltiplos agentes especializados, orquestrados por uma inteligência central (Supervisor).

A arquitetura foi atualizada para utilizar as tecnologias "State-of-the-Art" de Dezembro de 2025, priorizando a estabilidade e o ecossistema robusto de ferramentas de IA.

### Mudanças Chave em Relação ao Esboço Original:
1.  **Agentes em Python:** O núcleo de inteligência (Agentes, Crews, Tools) será desenvolvido em **Python** (não TypeScript).
    *   *Justificativa:* Frameworks como CrewAI e LangGraph têm suas versões primárias e mais avançadas em Python. Para alcançar a "melhor implementação possível", o Python oferece acesso nativo às bibliotecas de ML/AI (PyTorch, Pandas, Scikit-learn) e suporte de primeira classe dos LLMs.
2.  **Infraestrutura Simplificada:** Remoção inicial de Kubernetes/Docker para focar na lógica de agentes e agilidade de desenvolvimento.
3.  **Modelos Atualizados:** Suporte nativo para **GPT-4o** (OpenAI) e **Gemini 2.0/1.5 Pro** (Google).

---

## 2. Stack Tecnológico (Dezembro 2025)

### Backend de IA (Core) - `backend-ai/`
*   **Linguagem:** Python 3.11+
*   **Framework de Agentes:** CrewAI 1.7.0+ (Orquestração de Roles e Tasks)
*   **Controle de Fluxo:** LangGraph (para fluxos de supervisão complexos e stateful)
*   **API Framework:** FastAPI (Exposição dos agentes via REST)
*   **LLMs:**
    *   `gpt-4o` (Raciocínio Complexo/Supervisor)
    *   `gemini-2.0-flash` (Alta velocidade/Tarefas repetitivas)
*   **Memória:** Memória de Curto Prazo (In-memory/SQLite) e Longo Prazo (ChromaDB/Qdrant local).

### Frontend / Interface - `frontend-dashboard/`
*   **Framework:** Next.js 15 (React)
*   **Estilização:** Tailwind CSS + ShadcnUI
*   **Comunicação:** API REST (Consumindo o FastAPI)

---

## 3. Arquitetura de Pastas (Hybrid Monorepo)

```
julius-ai-agency/
├── docs/                   # Documentação do Projeto
├── backend-ai/             # [PYTHON] O Cérebro do Jules
│   ├── src/
│   │   ├── agents/         # Definição dos Agentes (Persona, Backstory)
│   │   ├── crews/          # Grupos de Agentes (Equipes por Setor)
│   │   │   ├── analysis/   # Setor de Análise
│   │   │   └── dev/        # Setor de Desenvolvimento
│   │   ├── tools/          # Ferramentas Customizadas (Search, Calculator)
│   │   ├── config/         # Arquivos YAML de configuração (prompts)
│   │   ├── api/            # Endpoints FastAPI
│   │   └── main.py         # Entrypoint
│   ├── tests/
│   ├── requirements.txt
│   └── .env
└── frontend-dashboard/     # [NODE] A Face do Jules (Futuro)
    ├── src/
    └── package.json
```

---

## 4. Design dos Agentes (CrewAI Pattern)

Cada "Setor" funcionará como uma **Crew** independente, que pode ser acionada pelo **Supervisor**.

### Exemplo: Setor de Análise (`AnalysisCrew`)
*   **Researcher:** Busca dados na web e em documentos internos.
*   **Data Analyst:** Processa os dados brutos, cria correlações.
*   **Insights Specialist:** Gera relatórios executivos baseados na análise.

### O Supervisor (Hierárquico)
O Supervisor é um meta-agente que recebe a requisição do usuário via API, decide qual Crew (Setor) deve ser acionado, e agrega a resposta final.

---

## 5. Próximos Passos de Implementação

1.  Configurar ambiente Python e dependências.
2.  Implementar o `AnalysisCrew` como prova de conceito (PoC).
3.  Implementar a API FastAPI para expor a Crew.
4.  Validar o fluxo completo: `Input Usuario -> API -> Crew -> LLMs -> Resposta`.
