# KI Systeme und Use Cases

Gemäß der KI-Definition des Europäischen Parllaments ist

> [Künstliche Intelligenz die Fähigkeit einer Maschine, menschliche Fähigkeiten wie logisches Denken, Lernen, Planen und Kreativität zu imitieren.](https://www.europarl.europa.eu/topics/de/article/20200827STO85804/was-ist-kunstliche-intelligenz-und-wie-wird-sie-genutzt)

Aufbauend auf obiger Definition teilen wir KI Systeme in drei Kathegorien ein. Sie weisen unterschiedliche Fähigkeiten auf, die bei der Umsetzung von KI Use Cases von Bedeutung sind.

<img src="../ki_systeme.png" width="600" height="600" />

Je höher der Grad an Autonomie und Spezialisierung, desto komplexer gestaltet sich die Umsetzung des KI Use Cases und desto mehr Komponenten der KI Plattform werden für diese benötigt.

## Conversational AI

Wir sprechen von einem Conversational AI Use Case, wenn eine KI mit einem Menschen eine Konversation führen kann, bei der der Mensch nicht mehr unterscheiden kann, ob er mit einer KI oder einem Menschen kommuniziert. KI mimikt Konversation.

Conversational AI bezieht sich somit auf Technologien, die es Maschinen ermöglichen, natürliche Gespräche mit Menschen zu führen. Diese Technologien nutzen Methoden der künstlichen Intelligenz, um Sprache zu verstehen, zu verarbeiten und zu generieren. Hier sind einige zentrale Aspekte. Conersational AI Use Cases nutzen dabei folgende Technologien:

- Sprachverarbeitung: Conversational AI verwendet Natural Language Processing (NLP), um gesprochene oder geschriebene Sprache zu interpretieren.

- Dialogmanagement: Die Systeme können den Kontext eines Gesprächs verfolgen und relevante Antworten generieren, um eine flüssige Interaktion zu ermöglichen.

- Lernfähigkeit: Viele Conversational-AI-Systeme nutzen maschinelles Lernen, um aus Interaktionen zu lernen und ihre Antworten im Laufe der Zeit zu verbessern.

Conversational AI Use Cases sind oft horizontale Use Cases, die auf eine breite Benutergruppe zugeschnitten sind. Das Dialogmanagement (Chat Frontend) ist von zentraler Bedeutung. Es wird häufig mit einem starken LLM und einem RAG kombiniert, um intelligente Auskunftssysteme zu erstellen. 

## Copilot

Ein Copilot unterstützt den Menschen in seinen Aufgaben. Ein Copilot integriert sich in den Arbeitsablauf und benötigt dazu Wissen über den Kontext des Benutzers bei seiner Aufgabe.

Er muss folgende Fähigkeiten besitzen:

- Antizipation der Intensionen des Bernutzers: Copiloten können Benutzerbedürfnisse vorhersehen und proaktiv Vorschläge oder Erinnerungen auf der Grundlage von Mustern und früheren Interaktionen anbieten.

- Teilen des Arbeistgedächtnisses: Copiloten können große Mengen an Daten analysieren und Erkenntnisse liefern, die den Nutzern helfen, fundierte Entscheidungen auf der Grundlage von Daten zu treffen.

- Kontextbezogenes Verstehen: Copiloten können den Kontext einer Aufgabe oder eines Gesprächs verstehen, so dass sie relevante Vorschläge oder Informationen liefern können.

- Automatisierung von Aufgaben: Copiloten können sich wiederholende Aufgaben automatisieren, z. B. die Planung von Besprechungen oder die Erstellung von Berichten, so dass sich die Benutzer auf komplexere Tätigkeiten konzentrieren können.

- Lernen aus Interaktionen: Copiloten können im Laufe der Zeit aus den Interaktionen der Nutzer lernen, ihre Leistung verbessern und die Antworten auf individuelle Präferenzen abstimmen.

- Integration mit Tools: Copiloten können in andere Softwareanwendungen und Tools integriert werden, um deren Funktionalität zu verbessern und die Arbeitsabläufe zu optimieren.

Ein Copilot kann ein Fachverfahren um KI Services erweitern. Dabei assistiert der Copilot den Benutzer in den Use Cases des Fachverfahrens  mit dem Ziel diese effizienter abzuarbeiten.

## Multi Agent Problem Solver

Systeme zur Lösung von Problemen, bei denen mehrere autonome Agenten interagieren und zusammenarbeiten, um bestimmte Ziele zu erreichen, nennen wir Multi-Agent Problem Solver.  

- Agenten: Jeder Agent arbeitet unabhängig, mit eigenen Zielen, eigenem Wissen und eigenen Entscheidungsfähigkeiten. Sie sind speialisierte Softwareprogramme.

- Planung: In der Regeln ist ein Agent für die Planung zur Lösungsfindung verantwortlich. Er muss den Problem-Kontext verstehen und eine Lösungsstrategie entwickeln, um dann andere spezialisierte Agenten mit Aufgaben zu versehen.

- Kollaboration: Um komplexe Probleme zu lösen, die ein einzelner Agent nicht selbstständig lösen kann, müssen Agenten zusammenarbeiten, Informationen austauschen und ihre Aktionen koordinieren.

- Kommunikation: Effektive Kommunikationsprotokolle sind entscheidend für Agenten, um Informationen auszutauschen, zu verhandeln und gemeinsame Entscheidungen zu treffen.

- Verteiltes Lösen von Problemen: Multiagentensysteme verteilen den Problemlösungsprozess und ermöglichen so Skalierbarkeit und Flexibilität.  Dies ist besonders in dynamischen Umgebungen nützlich, in denen sich die Bedingungen schnell ändern.

- Lösung von Konflikten: Agenten können konkurrierende Interessen oder Ziele haben, was Konfliktlösungsstrategien erforderlich macht, um einen Konsens oder eine optimale Lösung zu erreichen.

- Algorithmen: Verschiedene Algorithmen, wie z. B. Spieltheorie, Auktionsmechanismen und Konsensprotokolle, werden eingesetzt, um die Zusammenarbeit und Entscheidungsfindung zwischen Agenten zu erleichtern.

Treten innerhalb eines Fachverfahrens Problemstellungen auf, für die es keinen vordefinierten Lösungsweg gibt, bzw. sich der Lösungsweg erst aus der Analyse des Sachverhalts ergibt, kann ein Multi-Agent Problem Solver ein guter Kandidat für die Umsetzung eines KI Use Cases sein.
