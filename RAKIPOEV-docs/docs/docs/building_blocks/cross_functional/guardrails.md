# Leitplanken

Die Referenzarchitektur muss Leitplanken (Guardrails) implementieren. Es wird zwischen Input-Guardrails und Output-Guardrails unterschieden:

## Input-Guardrails

Input-Guardrails bieten Schutz vor folgenden Risiken:

- unbeabsichtigter Veröffentlichung privater (zu schützender) Informationen (DSGVO), insbesondere an externe API
- Model Jailbtreaking (Prompts die das System kompromittieren können)
- Verhinderung von gefährlichen und nicht-ethischen Prompts

## Output-Guardrails

Output-Guardrails bieten Schutz vor folgenden Risiken:

- Fehlgeschlagende Prompts und falsche Antworten
- Toxische Antworten
- Halluzinationen
- Sensitive Informationen (aus RAG Systemen), die nicht öffentlich gemacht werden dürfen

## Open-Source-Ansätze für Guardrails:

- [Guardrails-AI](https://github.com/guardrails-ai/guardrails)
- [NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
