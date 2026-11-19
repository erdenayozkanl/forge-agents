# ForgeAgents — Auditable Research Workflow

A functional multi-step **planner → researcher → writer → verifier** workflow, with bounded, read-only document retrieval, an inspectable LangGraph topology, optional local Ollama writer, per-step tracing, local JSON checkpoints, and an HTTP API. Documents are synthetic and links are **illustrative placeholders, not live references**.

## Run locally (Python 3.11+)

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py "How should we evaluate hybrid search?"
python main.py --serve
# POST http://127.0.0.1:8002/run {"task":"How should we evaluate retrieval?"}
pytest -q
```

Container API: `docker compose up --build` (port 8002). Run artifacts are mounted to `./runs`.

Works offline without API keys. In default mode the planner is a fixed deterministic policy, the researcher searches local docs, the writer extracts evidence, and the verifier checks **citation-number validity only**. This is a working orchestration baseline, not a fully autonomous LLM multi-agent framework.

## Optional local LLM

Install/start [Ollama](https://ollama.com/), then `ollama pull llama3.2`. Run `python main.py "..." --ollama` to synthesize a report using the local model. Requires sufficient RAM and downloaded weights. This version does not give the LLM arbitrary tool execution rights.

## Engineering backlog

For a stronger production agent portfolio: add real LangGraph supervisor and specialist nodes, typed tool calls, intent-scoped permissions, max-step budgets, prompt-injection adversarial suite, HITL approval for writes, durable queue, OpenTelemetry, retries with idempotency, evaluator datasets, answer faithfulness testing, and human review. Do not treat the basic verifier as semantic fact checking.
