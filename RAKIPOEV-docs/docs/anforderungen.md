# Anforderungen

Die Plattform für generative KI muss zentrale Anforderungen wie geringe Inferenzzeiten, hohe
Skalierbarkeit, Flexibilität und die Entkopplung einzelner Komponenten erfüllen. Die 
Architektur muss erlauben, jede Komponente unabhängig voneinander zu betreiben, was zukünftige
technologische Entwicklungen und den Austausch von Modulen durch leistungsfähigere
Lösungen erleichtert. 
Im Sinne der digitalen Souveränitätä liegt ein weiterer Fokus auf der Nutzung von Open-Source-Technologien.
Da der technologische Fortschritt im Bereich generativer KI äußerst schnelllebig ist, ist eine
strikte Trennung der Architektur in modulare, eigenständige Bausteine entscheidend. Diese
Trennung erlaubt es, spezifische Teile der Plattform bei Bedarf durch fortschrittlichere
Technologien zu ersetzen, ohne dabei die gesamte Architektur verändern zu müssen.

| Nr. | Anforderung |
| --- | ----------- |
| 1 | Mandantenfähigkeit |
| 2 | Benutzerverwaltung |
| 2.1 | Benutzerprofil |
| 2.2 | Prompt-Historie |
| 2.3 | Token-Usage |

## Funktionale Anforderungen

|Kategorie|Use Case||
|---------|--------||
|Texterzeugung|Texte übersetzen|Ermöglicht die präzise automatische Übertragung von Inhalten zwischen verschiedenen Sprachen.
||Texte zusammenfassen|Reduktion von längeren Texten auf ihre wesentlichen Kernaussagen, um die Hauptpunkte und wichtigsten Informationen prägnant darzustellen.
||Texte umformulieren |Bestehende Texte durch Umstrukturierung und Wortwahländerungen neu formulieren, um den Inhalt klarer, ansprechender oder zielgruppenspezifischer zu gestakten, ohne die ursprüngliche Bedeutung zu verlieren.
||Texte in einfache Sprache umformulieren |Erleichtert das Verständnis komplexer Inhalte, indem schwierige Begriffe und Satzstrukturen vereinfacht werden.
||Texte generieren|Texte erstellen, basierend auf vorgegebenen Themen oder Eingaben.. Dabei Unterscheidung mit Vorlage (bspw. Vermerk) oder ohne Vorlage (bspw. Freitext).
||Texte bewerten (Plausibilität, etc.)|Analyse und Bewertung von Texten auf Plausibilität, Relevanz und Kohärenz, um die Qualität und Genauigkeit sicherzustellen.
||Texte befragen|Informationen aus umfangreichen Texten extrahieren, indem spezifische Fragen gestellt und relevante Antworten identifiziert werden.
||Texte erläutern|Analysieren und Erklären von Textinhalten, um die Bedeutung und Zusammenhänge klar und verständlich darzustellen.
||Texte vergleichen|Bewertung unterschiedlicher Perspektiven (Texte) zu einem Thema, z. B. Benennung von Vor- und Nachteilen
||Ratschläge erhalten|Perspektiven beleuchten, um fundierte Entscheidungen zu treffen und Probleme effektiver zu lösen.
|Textsuche|In Texten suchen |Auffinden spezifischer Informationen in großen Textmengen.
||Texte recherchieren |Suchen, Analysieren und Auswerten von schriftlichen Quellen zur Gewinnung relevanter Informationen und Erkenntnisse.
||Texte vergleichen (Ähnlichkeiten)|Zueinander ähnliche Texte identifizieren, z. B. mit dem Ziel der Kategorisierung
|Bilderzeugung|Bilder erstellen|Auf Basis von Texten 
|||Auf Basis von Audio
|||
||Bilder in Dokumente integrieren|Integration in Office-Dokumente wie Schreiben oder auch Foliensätze.
|Bilderkennung|Bilder beschreiben |Als Text
|||Als Audio
||Bilder vergleichen|Bspw. Vorher / Nachher Vergleich
|||Fehlersuche
|||Erkennung von Anomalien
|Spracherkennung|Sprache erkennen|Audio oder Texteingabe wird erkannt 
||Sprache als Text |Spracheingabe (in Audio) kann als Text wiedergegeben werden
|Spracherzeugung|Sprache als Audio|Spracheingabe (in Text) kann als Audio wiedergegeben werden
||Sprache als Text|Spracheingabe (in Audio) kann als Textwiedergegeben werden
|Videoerzeugung||Generierung von Videomaterial basierend auf Eingaben. 
|Videoerkennung||Analyse und Interpretation von Videomaterial zur weiteren Verarbeitung oder Erkennung von Anomalien.
|Fachspezifische Funktionen|Datenmuster erkennen|Identifizieren von Trends und Zusammenhängen in großen Datensätzen zur Unterstützung fundierter Entscheidungen und Vorhersagen.
||Vorhersagemodelle|Zukünftige Ereignisse oder Trends in verschiedenen Bereichen präzise vorhersagen und optimieren.
|Personal Assistants|Intelligente persönliche Assistenten|Unterstützen Benutzer durch automatisierte Prozesse oder Eingaben und Sprachbefehle bei anfallenden Aufgaben.
||Automatisierte Terminplanung und E-Mail-Verwaltung|Optimiert Zeitmanagement, indem sie Aufgaben effizient organisiert und zeitnahe, relevante Kommunikation gewährleistet.
|Simulationssysteme|Virtuelle Umgebungen für Trainingszwecke (in Kombination mit Augmented Reality?)|Realistische Simulationen, die das Erlernen komplexer Fähigkeiten sicher und effizient ermöglichen.
|Robotik|Steuerung und Navigation von Robotern|Präzise Bewegungsplanung, Hindernisvermeidung und autonome Entscheidungen in dynamischen Umgebungen für verschiedene Anwendungen.
|KI-Modelle auf Edge-Geräten (z.B. Smartphones, IoT-Geräte)|Offline KI|Implementation lokaler Sprachmodelle auf Edge-Geräten, um auch Offline-Anwendung zu ermöglichen (z.B. im Flugzeug).
|||
|Allgemeine Funktionen|Generierung stoppen|
||Text eingeben|
||Dokumente hochladen|
||Kontexte bilden|



### Vermeidung/Reduzierung von Halluzinationen


## Prinzipien der KI-Architektur / Nicht-Funktionale Anforderungen

### Modularisierung und Service-orientierte Architektur
Ein wesentliches Merkmal der KI-Plattform für die öffentliche Verwaltung ist die Austauschfähigkeit einzelner Komponenten mit dem Ziel, technische Weiterentwicklungen im Bereich der Künstlichen Intelligenz zeitnah un mit vertretbarem Aufwand berücksichtigen und integrieren zu können. Die damit einhergehende Modularisierung trägt dazu bei, dass Komponeten autark voneinander entwickelt werden können. Dies setzt verbindliche Vorgaben auf der Ebene der Makro-Architektur voraus.

### Erweiterbarkeit
Durch standardisierte Schnittstellen, einer konsequenten Microservices-Architektur und verbindlichen Architekturvorgaben soll die Erweiterbarkeit der KI-Plattform nicht nur durch die Implementierung zusätzlicher Use Cases garantiert werden, sondern auch neue, diesen Use Cases zugrunde liegende Funktionen, erfolgen können.

### Nutztung von Open Source-Komponenten
Die KI-Plattform für die öffentliche Verwaltung setzt vorrangig auf Open Source-Komponenten und profitiert damit von den stetigen Weiterentwicklungen im KI-Umfeld. Gleichzeitig stellt sie sicher, dass Ressourcen für den Aufbau der KI-Plattform effizient eingesetzt werden und redundante Entwicklungen ohne maßgeblichen qualitativen Vorteil vermieden werden.

### Bereitstellung als Open Source-Software:
Nach dem "Einer-für-Alle"-Prinzip (EfA-Prinzip) zielen sowohl die Konzeption der KI-Architektur für die öffentliche Verwaltung als auch die zueghörige Referenzimplementierung darauf ab, eine transparente Diskussionsgrundlage und technische Grundlage für KI-Kernfunktionen allgemein zur Verfügung zu stellen. Erweiterungen und Verbesserungen an der Architektur und Implementierung sollen in die Weiterentwicklung einfließen.

### Zentrales RAG-System
Aufgrund der starken dokumentorientierten Arbeitsweise in der öffentlichen Verwaltung ist ein grundlegendes Element der KI-Plattform ein zentrales RAG-System. Hierzu sollen vorrangig Open Source-Komponenten zum Einsatz kommen, die einen vertrauenswürdigen Umgang mit Dokumenten der öffentlichen Verwaltung ermöglichen.

### Kapselung
Zusätzliche Abstraktionsebenen sorgen für eine Kapselung technischer Implementierungen und ermöglichen den parallelen Einsatz unterschiedlicher Lösungen. Dies gewährleistet die technische Unabhängigkeit der KI-Plattform von einzelnen Implementierungen.

### Verwendung von Open Source KI-Modellen
Ein wesentliches Merkmal der KI-Plattform für die öffentliche Verwaltung ist die Unabhängigkeit von externen Cloud-Angeboten. In diesem Sinne setzt sie auf die Verwendung qualitativ hochwertiger Modelle auf Basis eines Open Source-Lizenzmodells.

### On Premises-Betrieb
Die KI-Plattform der öffentlichen Verwaltung ist darauf ausgerichtet, On Premises auf eigenen Servern betrieben zu werden. Dies erlaubt die eigenständige Verarbeitung sensibler Daten innerhalb des eigenen Rechenzentrums und wahrt die digitale Souveränität beim Einsatz von KI.

### Mandantenfähigkeit
Eine Trennung nach unterschiedlichen Organisationen bzw. Organisationseinhaiten stellt sicher, dass Zugriffe ausschließlich im vorgegebenen Rahmen erfolgen können.

### Nutzerverwaltung, Rollen und Berechtigungen
Durch die Berücksichtigung von Rollen und Berechtigungen auf Nutzerebene sind individuelle Funktionen und Anpassungen möglich. Darüber hinaus lässt sich eine Abgrenzung der Zugriffsberechtigungen vornehmen. Bei der Anbindung von Systemen bzw. der Überführung von Daten bleiben an dieser Stelle bereits definierte Berechtigungen erhalten.

