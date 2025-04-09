# Allgemeine Anforderungen

Ziel der KI-Plattform ist es die **Entwicklung, die Integarion und den Betrieb** von **horizontalen und vertikalen (Gen)AI Uses Cases** für die öffentliche Verwaltung zu ermöglichen.

**Horiziontale Use Cases** sind solche, die von der Mehrheit der Mitarbeitenden genutz werden (bspw. allgemeine Verwaltungsaufgaben, wie das Bearbeiten von Bürgeranfragen, oder das Erstellen von Vermerken). **Vertikale Use Cases** hingegen betreffen spezielle fachliche Bereiche, dessen Benutzerkreis eingeschränkt ist. 

Die bereitgestellten KI-Services müssen für die Mitarbeitenden über ein **Web Frontend** aufrufbar sein, zusätzlich aber auch über **Plugins** in vorhandenen Office-Anwendungen, inklusive E-Mail-Anwendung. Ergänzend erfordern insbesondere vertikale Use Cases den Zugriff der erforderlichen KI-Services über das **Fachverfahren** selbst.

Die Plattform für generative KI muss zentrale Anforderungen wie **geringe Inferenzzeiten, hohe Skalierbarkeit, Flexibilität und die Entkopplung einzelner Komponenten** erfüllen.

Die  Architektur muss erlauben, jede **Komponente unabhängig voneinander zu betreiben**, was zukünftige technologische Entwicklungen und den Austausch von Modulen durch leistungsfähigere Lösungen erleichtert.

Im Sinne der digitalen Souveränität liegt ein weiterer Fokus auf der **Nutzung von Open-Source-Technologien**.

Da der technologische Fortschritt im Bereich generativer KI äußerst schnelllebig ist, ist eine strikte Trennung der Architektur in **modulare, eigenständige Bausteine** entscheidend. Diese Trennung erlaubt es, spezifische Teile der Plattform bei Bedarf durch fortschrittlichere Technologien zu ersetzen, ohne dabei die gesamte Architektur verändern zu müssen.

**Modularität und Wiederverwendbarkeit** bilden das Grundprinzip beim der Implementierung horizontaler und vertikaler Use Cases. Die Plattform soll es ermöglichen, dass diese aus bereits bestehenden oder neuen Komponenten zusammengebaut werden können.

Ist ein Use Case einmal implementiert, kann er von anderen Benutzern der Plattform über einen "Use Case Shop" im Rahmen von open source angepasst und wiederverwendet werden.




