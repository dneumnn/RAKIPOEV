# Vom Einfachen zum Komplexen

Bei der Entwicklung eines KI-Use Cases empfehlen wir folgende Vorgehensweise:

- Konzentration auf den Chat-Dialog mit einem Modell. Enthält das Modell nicht das erforderliche Wissen, um Fragen eines Benutzers zu beantworten, dann 
- Erweitere den Chat um Kontext mittels eines RAG-Ansatzes
- Füge in jedem Fall Guardrails hinzu, um die KI-Anwendung sicherer zu machen.
- Nutze ein LLM-Gateway um den Zugriff auf LLMs zu professionalisieren. Hier lassen sich nicht nur Guardrails verankern, sondern ebenfalls das Tacking der Nutzer, das Tracing von Anfragen und Antworten, sowie ein allumfassendes Logging.
- Nutze Caching zur Steigerung der Performanz. Dies lässt sich über geeignete Inference-Engines ermöglichen.
- Setze KI-Agenten ein, um weitere Automatisierung und vertikale Integration in Fachverfahren weiter zu optimieren. 
- Integriere allumfassende Observability und nutzte diese für ein end-2-end Testing und Hardening der LLM-Anwendung.
