# Leitlinien der KI-Architektur

## Modularisierung und Service-orientierte Architektur

Ein wesentliches Merkmal der KI-Plattform für die öffentliche Verwaltung ist die Austauschfähigkeit einzelner Komponenten mit dem Ziel, technische Weiterentwicklungen im Bereich der Künstlichen Intelligenz zeitnah un mit vertretbarem Aufwand berücksichtigen und integrieren zu können. Die damit einhergehende Modularisierung trägt dazu bei, dass Komponeten autark voneinander entwickelt werden können. Dies setzt verbindliche Vorgaben auf der Ebene der Makro-Architektur voraus.

## Erweiterbarkeit

Durch standardisierte Schnittstellen, einer konsequenten Microservices-Architektur und verbindlichen Architekturvorgaben soll die Erweiterbarkeit der KI-Plattform nicht nur durch die Implementierung zusätzlicher Use Cases garantiert werden, sondern auch neue, diesen Use Cases zugrunde liegende Funktionen, erfolgen können.

## Nutztung von Open Source-Komponenten

Die KI-Plattform für die öffentliche Verwaltung setzt vorrangig auf Open Source-Komponenten und profitiert damit von den stetigen Weiterentwicklungen im KI-Umfeld. Gleichzeitig stellt sie sicher, dass Ressourcen für den Aufbau der KI-Plattform effizient eingesetzt werden und redundante Entwicklungen ohne maßgeblichen qualitativen Vorteil vermieden werden.

## Bereitstellung als Open Source-Software

Nach dem "Einer-für-Alle"-Prinzip (EfA-Prinzip) zielen sowohl die Konzeption der KI-Architektur für die öffentliche Verwaltung als auch die zueghörige Referenzimplementierung darauf ab, eine transparente Diskussionsgrundlage und technische Grundlage für KI-Kernfunktionen allgemein zur Verfügung zu stellen. Erweiterungen und Verbesserungen an der Architektur und Implementierung sollen in die Weiterentwicklung einfließen.

## Zentrales RAG-System

Aufgrund der starken dokumentorientierten Arbeitsweise in der öffentlichen Verwaltung ist ein grundlegendes Element der KI-Plattform ein zentrales RAG-System. Hierzu sollen vorrangig Open Source-Komponenten zum Einsatz kommen, die einen vertrauenswürdigen Umgang mit Dokumenten der öffentlichen Verwaltung ermöglichen.

## Kapselung

Zusätzliche Abstraktionsebenen sorgen für eine Kapselung technischer Implementierungen und ermöglichen den parallelen Einsatz unterschiedlicher Lösungen. Dies gewährleistet die technische Unabhängigkeit der KI-Plattform von einzelnen Implementierungen.

## Verwendung von Open Source KI-Modellen

Ein wesentliches Merkmal der KI-Plattform für die öffentliche Verwaltung ist die Unabhängigkeit von externen Cloud-Angeboten. In diesem Sinne setzt sie auf die Verwendung qualitativ hochwertiger Modelle auf Basis eines Open Source-Lizenzmodells.

## On Premises-Betrieb

Die KI-Plattform der öffentlichen Verwaltung ist darauf ausgerichtet, On Premises auf eigenen Servern betrieben zu werden. Dies erlaubt die eigenständige Verarbeitung sensibler Daten innerhalb des eigenen Rechenzentrums und wahrt die digitale Souveränität beim Einsatz von KI.

## Mandantenfähigkeit

Eine Trennung nach unterschiedlichen Organisationen bzw. Organisationseinhaiten stellt sicher, dass Zugriffe ausschließlich im vorgegebenen Rahmen erfolgen können.

## Nutzerverwaltung, Rollen und Berechtigungen

Durch die Berücksichtigung von Rollen und Berechtigungen auf Nutzerebene sind individuelle Funktionen und Anpassungen möglich (Benutzerprofil). Darüber hinaus lässt sich eine Abgrenzung der Zugriffsberechtigungen vornehmen. Bei der Anbindung von Systemen bzw. der Überführung von Daten bleiben an dieser Stelle bereits definierte Berechtigungen erhalten.

## Usage

Bei der Verwenung von LLM-Aufrufen muss der Token-Verbrauch überwacht werden können, um einen unbeabsichtig oder beabsichtigt hohen Verbrauch einschränken zu können. Der Token-Verbrauch kann auch als Abrechnungs bzw. Verrechnungsmodell genutzt werden.

## Vermeidung/Reduzierung von Halluzinationen

Zusammengesetzte KI-Anwendung, welche auf LLMs als zentrale Bestandteile setzen unterliegen der Statistik der zugrundeliegenden LLMs. Diese sind "next-word-predictor" und damit ist Halluzination ein wesentliches Merkmal, das man durch geeignete Mechanismen kontrollieren kann. Halluzination tritt auf verschiedene Weisen in Kraft: Der Prompt liegt "out-of-distribution", er beinhaltet im Training nicht gesehene Tokens und das LLM kann auf Basis seines Fakten-basierten Wissen keine sinnvolle (gültige) Prognose für ein nächstes Wort treffen und triftet in eine Pfad-Abhängigkeit ab, die wir dann als Halluzination wahrnehemen. Ziel der Plattform ist es Vermeidungsstrategien gegen Halluzination bereitzustellen.
