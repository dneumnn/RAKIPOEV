# Building Blocks

## Frontends

Dieser Layer umfasst die Benutzeroberflächen für Administratoren und Endnutzer, welche auf die KI-Dienste zugreifen und sie verwalten können.

### Chat-Frontend

Das Chat-Frontend ist eine benutzerfreundliche Web-Anwendung die es ermöglicht mit mit großen Sprachmodellen (LLMs) zu interagieren.

Dabei werden folgende Anforderungen an die Benutzerschnittstelle gestellt:

- SSL-Fähigkeit
- Authentifizierung über einen Identity-Provider (z.B. [Keycloak](https://www.keycloak.org))
- Die Anwendung sollte [The Twelve-Factor App](https://12factor.net/de/)-Prinzipien genügen. Insbesondere die Nebenläufigkeit und die Zustandslosigkeit sind für einen Beztrieb der Anwendung in einer cloud-nativen Umgebung essentiell.
- Mandantenfähigkeit
- Das Look&Feel sollte auf das Look&Feel einer Behörde angepasst werden können
- Die Anwendung genügt den wesentlichen Anforderungen an [Barrierefreiheit](https://www.behindertenbeauftragter.de/DE/AS/schwerpunkte/barrierefreiheit/barrierefreiheit-node.html1) 
- Die Anwendung ermöglicht Persistenz des Chat-Verlaufs je Benutzer
- Über Pipelines, die das [Pipes & Filter](https://de.wikipedia.org/wiki/Pipes_und_Filter)-Muster implementieren kann der Prompt vor und nach-bearbeitet werden. Zur Vor- und Nachbearbeitung können die Service-Komponenten RAG, Tools, Tasks oder Agents benutzt werden.

![image](../assets/Chat-Anwendung.png)

### Admin-Frontends

- KI-Service Admin UI: Diese Schnittstelle ermöglicht Administratoren die Verwaltung
und Konfiguration der KI-Dienste.
- System Admin UI: Schnittstelle für die systemweite Verwaltung und Überwachung der
Plattform.

### Office-Plugins

### Anbindung von Fachverefahren über API

## Services

### Retrieval-Augmented-Generation

### Task-driven Services

### Tools

### Agenten-Pool

### Prompt-Store

## Modelle

### LLM-Gateway

### Modell-Runtimes

### Model-Store

## IAM Services

Zur Anbindung der Plattform empfiehlt sich im Sinne einer konsequenten Open-Source-Strategie ein Keycloak in der entsprechenden Cloud-Plattform.

## AI Platform

Die zentrale Plattformkomponente, die für das Management, die Entwicklung und Bereitstellung von Use Cases verantwortlich ist. Sie integriert mehrere wesentliche Funktionen:

- Monitoring: Überwachung der Plattformkosten, Nutzung und Performance.
- API-Gateway: Schnittstelle für den Zugriff auf die verschiedenen KI-Dienste.
- Use Cases & Services: Bereitstellung von verschiedenen KI-basierten Services wie Newsletter-Generierung, Voice Output, Zusammenfassung, Übersetzung, Bildgenerierung und Sprachausgabe.
- RAG – System basiert auf dem RAGFlow-Framework, das die Arbeit mit eigenen Dokumenten ermöglicht.
- Knowledge Base: Diese umfasst verschiedene Datenbanken wie Vektor-DB, Graph-DB und relationale DBs zur Speicherung und Nutzung von Wissensressourcen.

## ML Operations

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

