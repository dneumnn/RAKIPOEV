# High-Level-Architektur

Folgende Darstellung zeigt die High-Level-Referenzarchitektur in 3 Schichten (Layer), die untenstehend  näher beschrieben werden.

![](high_level_architecture.drawio)

Die (Referenz-)implementierung sollte so gestaltet werden, dass alle Komponenten cloud-nativ auf einem Kubernetes-Cluster betrieben werden können.

Komponenten der Referenzarchitektur lassen sich in drei Layer einteilen. Eine besondere Herausforderung bei der Implemetierung der verschiedenen Komponenten (Building Blocks) innerhalb der Layers liegt in der föderierten Benutzer- und Modell-Verwaltung. Diese wird im Kapitel [Datenmanagement](data_management.md) beschrieben.

## Frontend-Layer

Die Referenzarchitektur sieht verschiedene Frontends vor. Der Frontend-Layer umfasst die Benutzeroberflächen für Administratoren und Endnutzer, welche auf die KI-Dienste zugreifen und sie verwalten können.

Als "offensichtlichste" seien genannt:

- ein Chat-Frontend,
- Fachverfahren
- Office-PlugIn
- ein Admin-Frontend

Alle Frontends können über das API-Gateway auf die verschiedenen Services zugreifen.

## Services-Layer

Der Services-Layer beinheltet zustandslose funktionale Bausteine die sich zu Use Cases kombinieren lassen. Services sind über das API-Gateway aufrufbar. Integriert im API-Gateway ist eine Service-Registry. Das API-Gateway dient außerdem als Load Balancer für die Service-Aufrufe.

Folgende erste Servicearten sind identifziert:

- **RAG**: Über [RAGs](glossar.md#RAG) können mit Hilfe domänen-spezifische Datenquellen die Antworten für einen bestimmten Kontext verbessert werden. Die RAGs können z.B. mit RAGFlow umgesetzt werden. *Beispiel: der Service "DocumentSearch".*

- **Tools:** sind verschiedene Werkzeuge, die keinen Zugriff auf [Large Language Models](glossar.md#Large Language Model) benötigen. *Beispiele: ein Taschenrechner, Websuche oder das aktuelle Wetter*.

- **Task based Services:** stellen auf Basis von LLMs Funktionen zur Verfügung. *Beispiele: Summarization, Planning und Reasoning"*.

- **Agents**  sind Services, die autonom oder semi-autonom eine Aufgabe erfüllen. Die Aufgaben-Steuerung kann eintweder durch eine SOP (Standard Operating Procedure) vorgegeben werden oder mittels LLM in einem Planungs-Task erzeugt werden. Ein Agent kann sich dann je nach Aufgabe anderer Services bedienen.

## Inference-Layer

Der Inference Layer ist für die Verwaltung und Ausführung von Modellen verantwortlich.

