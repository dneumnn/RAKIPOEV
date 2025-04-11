# Model Registry

Die Verwaltung der Modelle muss folgende Anforderungen erfüllen:

- Freigabe-Workflow für neue Modelle
- Modell-Attribute, Prompt-Template, Default-System-Prompt, Default-Aufrufparameter müssen in Datenbank gespeichert werden können.
- Modell-Parameter muss über einen Object-Store (z.B. S3) verfügbar gemacht werden können.
- Berechtigungsverwaltung: wer darf welches Modell nutzen: Anwendung, Organisation, Team, (Benutzer).
