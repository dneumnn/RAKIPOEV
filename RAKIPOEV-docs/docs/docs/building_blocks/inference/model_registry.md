# Model Registry

Die Verwaltung der Modelle muss folgende Anforderungen erfüllen:

- Freigabe-Workflow für neue Modelle
- Modell-Attribute, Prompt-Template, Default-System-Prompt, Default-Aufrufparameter müssen in Datenbank gespeichert werden könen.
- Modell-Parameter muss über einen Object-Store (z.B. S3) verfügbar gemacht werden können.
- Berechtigungsververwaltung: wer darf welches Modell nutzen: Anwendung, Organisation, Team, (Benutzer).
