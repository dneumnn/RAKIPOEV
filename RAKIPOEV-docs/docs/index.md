# Exposee

Analog zur Architektur von Gebäuden stellen wir eine Bauprojektdarstellung einer KI-Plattform für die Öffentliche Verwaltung vor. Das Exposee beschreibt das Warum, das Was und das Wie in Form einer Referenzarchitektur sowie einer Referenzimplementierung.

## Warum

Horizontale und vertikale KI Anwendungsfälle bergen ein enormes Potenzial für die Effizienzsteigerung in der öffentlichen Verwaltung. Mit ihrer Hilfe lassen sich wirksame Entlastung für knappes Fachpersonal bewerkstelligen.

Wohingegen horizomtale Anwendungsfälle eine breite Anwenderschaft bei ihrer Arbeit unterstützen, sind vertikale Anwendungsfälle in Fachverfahren integrierte und versprechen die höcheten Effizienzgewinne.

Für eine zielgerichtete und kosten-effiziete Implementierung unter Wahrung der Souverenität ist eine Plattform notwenig, die

1. flächendeckend eingesetzt,
2. flexibel erweitert und
3. on-premise betrieben werden kann.

Sie sollte vollständig auf open-source und Standards Bausteinen aufbauen. Suie sollt gemeinschaftlich erweitert werden können, im Sinne einer basisplattform mit Plugin- und App-Store- und Serviceregistry-Konzept.

KI-Plattform bedeutet die Abkehr vom einfachen Einsatz eines Chatbots, der ein sehr großes Sprachmodell mit einer Oberfläche kapselt, hin zu intelligenten IT-Systemen, die Intelligenz im Zusammenspiel mit vieler KI Services und Modelle hervorbringt. Wir sehen diese Tendenz bei allen großen KI Herstellern und sind der Überzeugung, dass die öffentliche Verwaltung auch solch eine KI Plattform benötig, diese gemeinsam aufbauen kann und damit losgelöst von den großen Herstellern ihre Souveränität behaupten kann.

## Was

Die KI-Plattform soll Grundlage für Anwendungen aller Inteligenz-Stufen sein:

1. Vorhersagesysteme, Task-orientierte Services und Chatbots,
2. Assistenten und Co-Piloten sowie
3. eigenständig agierende Agenten.

Dabei ist es aufgrund der enormen Entwicklungsgeschwindigkeit des KI Ökosystems wichtig, dass die KI Plattform als zentrales Open Source Projekt gemeinsam von der öffentlichen Verwaltung entwickelt wird. Dafür muss die Plattform offen gegenüber Erweiterung und geschlossen gegenüber Veränderungen sein.

Wesentliche Bestandteile der KI-Plattform sind:

1. Inference Engines und Modell-Runtimes: Diese hosten Modell und erweitern sie durch einfache Routinen zur Generaierung ganzer Output-Streams.
2. Kapselung der Modell-Runtimes durch ein LLM-Gateway, welches einen standardisierten Zugriff (API), eine Authentifizierungs und Authorisierungsschicht sowie ein Verbrauchs-Tracking und Logging bereitstellt.
3. Agenten-Pool: Agenten können auf Basis eines App-Store-Konzeptes eingebracht und genutzt werden.
4. Task-driven Services: Bereitstellung einer Vielzahl von einfachen oder komplexen Tasks (z.B. Zusammenfassung, Übersetzung, Transkription, .... ) über ein Service-Gateway. Diese Services können von Chatbots, Fachverfahren, Agenten oder anderen Komponenten der Plattform genutzt werden.
5. Retrieval-Augmented-Generation: Anbindung eines oderer mehrerer RAG-Frameworks inklusive mandanten-fähiger Speicherverwaltung und Dokumenten-zentriertem Berechtigungssystem.
6. Verschiede Typen von Frontend-Technologien.
7. Prompt-Store
8. Model-Store

Horienzontle und Vertikale Anwendungsfälle entstehen durch geeignete Kombination der Bestandteile und können basierend auf der Referenzarchitektur beschrieben und implementiert werden. Blaupausen und Referenzimplementierungen werden in der Community geshared.

## Wie

Die Referenzarchitektur beinhaltet Design-Vorschläge für die einzelnen Komponenten.