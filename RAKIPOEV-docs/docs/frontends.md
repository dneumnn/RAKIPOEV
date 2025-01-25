# Frontends

Dieser Layer umfasst die Benutzeroberflächen für Administratoren und Endnutzer, welche auf die KI-Dienste zugreifen und sie verwalten können.

## Chat-Frontend

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

- Die Anwendung ermöglicht über ein Plug-In Konzept das Einbinden einer Vielzahl spezifischer Frontends in Abhängigkeit der Benutzer-Präferenzen. Auf diese Weise kann der Nutzer mehrere spezifische (vertiklale) Chat-Bot-Lösungen aus einer Benutzeroberfläche ansteuern. Dazu müssen Erweiterungspunkte (extension points) definert sein und gleichzeitig die Erweiterungsmöglichkeit über Konfiguration (im weitesten Sinne siehe auch [Fowler](https://martinfowler.com/eaaCatalog/plugin.html))

### Kandidaten für eine Implementierung

**[Open WebUI](https://openwebui.com)**

| Anforderung | Grad der Füllung |
| --- | ----------- |
| Open Source | BSD 3-Clause "New" or "Revised" License |
| SSL-Fähigkeit | aktuell nicht gegeben. SSL Terminierung muss über einen vorgeschalteten Server erfolgen ( z.B. Nginx, Apache, etc.) |
| Mandantenfähigkeit | nicht vorhanden |
| Authentifizierung via IDP | über Umgebungs-Variablen |
| Twelve-Factor-App | Session-Affinität kann über Konfiguration des Ingres-Controllers (Cookies) ermöglicht werden. |
| Look&Feel | anpassbar |
| Barrierefreiheit | unklar |
| Benutzerkonzept | Prompt-Historie, Nutzer-Präferenzen |
| Erweiterbarkeit durch Pipelines | vorhanden |
| Erweiterbarkeit durch Plugins | nicht vorhanden |

**[Quora POE](https://poe.com)**

Der Chat Client Poe von Quora zeuchnet sich durch Erweiterbarkeit mittels Plugins aus. Da es sich hier um closed-source handelt, dient dieser Eintrag nur zu Demonstrationszwecken für einen Frontend mit Plugin-Funktionalität.

| Anforderung | Grad der Füllung |
| --- | ----------- |
| Open Source | closed source, deshalb nur als Beispiel gelistet |
| Erweiterbarkeit durch Plugins | vorhanden |

Weitere erwähnenswerte open source Frontends sind:

- Der Chat Client von [RagFlow](https://ragflow.io) sowie
- das [LibreChat](https://www.librechat.ai).

## Admin-Frontends

- KI-Service Admin UI: Diese Schnittstelle ermöglicht Administratoren die Verwaltung und Konfiguration der KI-Dienste.
- System Admin UI: Schnittstelle für die systemweite Verwaltung und Überwachung der Plattform.

## Office-Plugins

## Anbindung von Fachverfahren über API
