# Cross-Funktionales

## IAM Services

Zur Anbindung der Plattform empfiehlt sich im Sinne einer konsequenten Open-Source-Strategie ein Keycloak in der entsprechenden Cloud-Plattform.

## Prompt-Store

## ML Operations

Dieser Layer umfasst die maschinellen Lernprozesse, die zur Entwicklung und Bereitstellung von
KI-Modellen notwendig sind.

- Data Processing & Training Pipelines: Datenverarbeitung und Training von Modellen erfolgen über automatisierte Pipelines.
- Deployment Pipelines: Automatisierte Bereitstellung von trainierten Modellen auf die Produktionsinfrastruktur.
- ML Deployments: Modelle werden auf GPUs in einer Kubernetes-Umgebung
bereitgestellt und verarbeitet.
- Inference Platform: Beinhaltet Inferenz-Engines, Sicherheitsvorkehrungen und die Stabilität der Bereitstellung von Modellen (z.B. durch Load Balancer und Ingress Controller). Teile dieser Plattform umfassen auch Sicherheitsmechanismen für Modelle, wie Guardrails sowie Systeme zur Überwachung und Protokollierung von Aktivitäten.
- Model Hub: Bereitstellung verschiedener Modelle wie Large Language Models (LLMs), Bildgenerierungsmodelle und Text-to-Speech (TTS)-Modelle.
- RESTful API: Der Zugriff wird durch eine RESTful-API gemäß dem OpenAI-Standard bereitgestellt.

## Kompositions-Fähigkeit
