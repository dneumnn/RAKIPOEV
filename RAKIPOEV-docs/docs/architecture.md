# Referenzarchitektur

## Anforderungen

Die Plattform für generative KI muss zentrale Anforderungen wie geringe Inferenzzeiten, hohe
Skalierbarkeit, Flexibilität und die Entkopplung einzelner Komponenten erfüllen. Die 
Architektur muss erlauben, jede Komponente unabhängig voneinander zu betreiben, was zukünftige
technologische Entwicklungen und den Austausch von Modulen durch leistungsfähigere
Lösungen erleichtert. 
Im Sinne der digitalen Souveränitätä liegt ein weiterer Fokus auf der Nutzung von Open-Source-Technologien.
Da der technologische Fortschritt im Bereich generativer KI äußerst schnelllebig ist, ist eine
strikte Trennung der Architektur in modulare, eigenständige Bausteine entscheidend. Diese
Trennung erlaubt es, spezifische Teile der Plattform bei Bedarf durch fortschrittlichere
Technologien zu ersetzen, ohne dabei die gesamte Architektur verändern zu müssen.

| Nr. | Anforderung |
| --- | ----------- |
| 1 | Mandantenfähigkeit |
| 2 | Benutzerverwaltung |
| 2.1 | Benutzerprofil |
| 2.2 | Prompt-Historie |
| 2.3 | Token-Usage |

## Nicht-Funktionale Anforderungen

## High-Level Architecture

### Applications

Dieser Layer umfasst die Benutzeroberflächen für Administratoren und Endnutzer, welche auf die KI-Dienste zugreifen und sie verwalten können.

- KI-Service Admin UI: Diese Schnittstelle ermöglicht Administratoren die Verwaltung
und Konfiguration der KI-Dienste.
- System Admin UI: Schnittstelle für die systemweite Verwaltung und Überwachung der
Plattform.
- User UI(s): Endbenutzer-Schnittstelle, welche die Interaktion mit den bereitgestellten
KI-Diensten, wie z.B. Chats, Bots oder Programm Plug-Ins ermöglicht.

### AI Platform
Die zentrale Plattformkomponente, die für das Management, die Entwicklung und Bereitstellung von Use Cases verantwortlich ist. Sie integriert mehrere wesentliche Funktionen:

- Monitoring: Überwachung der Plattformkosten, Nutzung und Performance.
- API-Gateway: Schnittstelle für den Zugriff auf die verschiedenen KI-Dienste.
- Use Cases & Services: Bereitstellung von verschiedenen KI-basierten Services wie Newsletter-Generierung, Voice Output, Zusammenfassung, Übersetzung, Bildgenerierung und Sprachausgabe.
- RAG – System basiert auf dem RAGFlow-Framework, das die Arbeit mit eigenen Dokumenten ermöglicht.
- Knowledge Base: Diese umfasst verschiedene Datenbanken wie Vektor-DB, Graph-DB und relationale DBs zur Speicherung und Nutzung von Wissensressourcen.

### ML Operations

Dieser Layer umfasst die maschinellen Lernprozesse, die zur Entwicklung und Bereitstellung von
KI-Modellen notwendig sind.

- Data Processing & Training Pipelines: Datenverarbeitung und Training von Modellen
erfolgen über automatisierte Pipelines.
- Deployment Pipelines: Automatisierte Bereitstellung von trainierten Modellen auf die
Produktionsinfrastruktur.
- ML Deployments: Modelle werden auf GPUs in einer Kubernetes-Umgebung
bereitgestellt und verarbeitet.
- Inference Platform: Beinhaltet Inferenz-Engines, Sicherheitsvorkehrungen und die
Stabilität der Bereitstellung von Modellen (z.B. durch Load Balancer und Ingress
Controller). Teile dieser Plattform umfassen auch Sicherheitsmechanismen für Modelle,
wie Guardrails sowie Systeme zur Überwachung und Protokollierung von Aktivitäten.
- Model Hub: Bereitstellung verschiedener Modelle wie Large Language Models (LLMs),
Bildgenerierungsmodelle und Text-to-Speech (TTS)-Modelle.
- RESTful API: Der Zugriff wird durch eine RESTful-API gemäß dem OpenAI-Standard
bereitgestellt.

### IAM Services

Zur Anbindung der Plattform empfiehlt sich im Sinne einer konsequenten Open-Source-Strategie ein Keycloak in der entsprechenden Cloud-Plattform. 

### Modell-Runtimes

### LLM-Gateway

### Agenten-Pool

### Task-driven Services

### Retrieval-Augmented-Generation

### Frontend-Technologien

### Prompt-Store

### Model-Store
