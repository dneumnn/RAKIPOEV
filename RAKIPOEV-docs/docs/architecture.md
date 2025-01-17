# High-Level-Architecture

Folgende Darstellung zeigt die High-Level-Referenzarchitektur in 3 Schichten, die untenstehend  näher beschrieben werden.

![](drawio/HighLevelArchitecture.drawio)

Die (Referenz-)implkementierung sollte so gestaltet werden, dass alle Komponenten als cloud-nativ auf einem Kubernetes-Cluster betrieben werden können.

## Frontends

Die Referenzarchitektur sieht verschiedene Frontends vor. Als "offensichtlichste" seien genannt 

- ein Chat-Frontend,
- Fachverfahren
- Office-PlugIn
- ein Admin-Frontend

Alle Frontends können über das API-Gateway auf die verschiedenen Services zugreifen.

## Services

Die Services sind über das API-Gateway aufrufbar. Integriert im API-Gateway ist eine Service-Registry. Das API-Gateway dient außerdem als Load Balancer für die Service-Aufrufe.

Folgende erste Servicearten sind identifziert:

* **Model Context Protocol**
* **RAG**: Über [<span class="textlink">RAGs</span>](glossar.md#RAG) können mit Hilfe domänen-spezifische Datenquellen die Antworten für einen bestimmten Kontext verbessert werden. Die RAGs können z.B. mit RAGFlow umgesetzt werden. *Beispiel: der Service "DocumentSearch".*
* **Tools:** sind verschiedene Werkzeuge, die keinen Zugriff auf [<span class="textlink">Large Language Models</span>](glossar.md#Large Language Model) benötigen. *Beispiele: ein Taschenrechner, Websuche oder das aktuelle Wetter*.
* **Task based Services:** stellen auf BAsis von RAGs oder LLMs Funktionen zur Verfügung. * Beispiele: Summarization, Planning und Reasoning"*.
* Agents

## Modelle

