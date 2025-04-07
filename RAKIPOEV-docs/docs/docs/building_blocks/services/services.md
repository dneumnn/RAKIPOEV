# Services

Services sind zustandslose funktionale Bausteine die sich zu Use Cases kombinieren lassen. Ziel ist es diese für die unterschiedlichen Use cases der öffentlichen Verwaltung wiederzuverwenden. Um dieses Ziel zu erreichen ist es notwendig, die Services nach einheitlichen Standards zu entwickeln, sie mit einem API zu versehen (über das sie gleichartig aufgerufen werden können) und als containerisierte Komponenten auszuliefern.

Wir unterscheiden vier Service Tpyen:

![image](services.png)

## Task

Ein Task ist ein Model-Task-driven Service. Hierbei wird eine spezifische Aufgabe mit einem spezifischen Modell ausgeführt. Dabei ist das Modell für die Aufgabe optimiert. Die Optimierung kann durch verschiedene Arten des Trainings (Supervised Finetuning, Reinforcement Learning, ..) erfolgen.

Ein Vielzahl von Model-Tasks und geeignete Modell finden sich auf [Hugging Face](https://huggingface.co/tasks).

Eine große Anzahl der in den Anforderungen beschriebenen Use Cases, wie z.B. Text Manipiulationen oder Translationen, lassen sich mit einem geeigneten Modell als Tasks umsetzen.

![image](task.png)

## Tool

Ein Tool ist ein Service mit dem das System mit seiner Aussenwelt (seinem Environment) interagieren kann. Im Gegensatz zu Tasks haben Tools keinen Zugriff auf ein Modell, dafür aber auf das Environment des Systems.

Typische Environments sind das Internet, Fachverfahren, aber auch eine Sandbox, in der Code ausgeführt werden kann.

![image](tool.png)

### Sandbox

Die sichere Ausführung von durch ein LLM erzeugten Code sollte entweder auf einer isolierten virtuellen Maschine oder über ein externes API (z.B. [E2B](https://e2b.dev)) erfolgen.

### MCP Server

Mithilfe des Model Context Protokolls (MCP) lassen sich verschiedene Datenquellen (Ressourcen, Tools, Templates) standardisiert an KI-Anwendungen anbinden. Die Komminkation erfolgt dabei bidrektional, so dass Datenquellen von einer KI-Anwendung gezielt angesprochen werden können, um bestimmte Informationen bereitzustellen. Diesen Zweck erfüllen MCP-Server, welche die Implemeniertung der Datenbereitstellung beinhalten. Die Anbindung von Tools kann somit über das Model Context Protokoll (MCP) standardisiert werden.

## Retrieval-Augmented-Generation

Retrieval-Augmented-Generation (kurz RAG ist ein komplexer Service, bei dem zu einem Prompt (Anfrage des Benutzers) Wissen aus vorhandenen Datenquellen selektiert, von dem man ausgeht, dass es als Faktenwissen in einem LLM nicht vorhanden ist. Der Prompt wird um das selektierte Wissen erweitert. Sowohl für das Retrieval, als auch für das Augmentation gibt es zahl reiche Umsetzungs-Muster, die innerhalb eines RAG angewandt werden können, um das gewünschte Ergebnis zu erzeugen.

Als Datenquellen werden je Aufgabe Vektor-Datenbanken, Graphen-Datenbanken, SQL-Datenbanken und Indexe (BM25) eingesetzt. Der Einsatz eines RAG bedingt einer vorgelagert Data-Pipeline, mithile derer man das Wissen geeignet aufbereitet in die ausgewählte Datenquelle überführt.

![image](rag.png)

RAG hat sich in den letzten zwei Jahres von einer einfachen Suche basierend auf Vector-Similarity (semantische Ähnlichkeit zwischen Text-Chunks) hin zu komplexeren graphen-basierten Verfahren weiterentwickelt.

|RAG|Idee|Vor- und Nachteile|
|---|----|------------------|
|[GraphRAG](https://microsoft.github.io/graphrag/)|--|--|
|[LiteRAG](https://github.com/HKUDS/LightRAG)|--|--|

### Kandidaten für die Implementierung

**[Haystack (deepset-ai)](https://github.com/deepset-ai/haystack)**

|Kriterium  |Bewertung|
|-----------|------------------|
|Lizenz     |Apache License 2.0|
|Einsatzzweck|Produktion|
|Skalierbarkeit|Ausgelegt für die Bearbeitung großer Dokumentenbestände|

**[RAGFlow (infiniflow)](https://github.com/infiniflow/ragflow)**

|Kriterium  |Bewertung|
|-----------|------------------|
|Lizenz     |Apache License 2.0|
|Einsatzzweck|Prototyping?|
|Skalierbarkeit|?|

**[txtai (neuml)](https://github.com/neuml/txtai)**

|Kriterium  |Bewertung|
|-----------|------------------|
|Lizenz     |Apache License 2.0|
|Einsatzzweck|Produktion|
|Skalierbarkeit|?|

**[STORM (stanford-oval)](https://github.com/stanford-oval/storm)**

|Kriterium  |Bewertung|
|-----------|------------------|
|Lizenz     |MIT Licence       |
|Einsatzzweck|Forschung (cutting edge technologies)|
|Skalierbarkeit||


## Agent

Ein Agent ist ein Service, der autonom oder semi-autonom eine Aufgabe erfüllt. Die Aufgaben-Steuerung kann eintweder durch eine SOP (Standard Operating Procedure) vorgegeben werden oder mittels LLM in einem Planungs-Task erzeugt werden. Ein Agent kann sich dann je nach Aufgabe anderer Services bedienen. 

[Vertikale Agenten](https://arxiv.org/abs/2501.00881) sind spezialisierte Agenten die neben dem LLM, das zur Aufgaben-Steuerung verwendet wird zusätzlich über ein Kurzzeit-Gedächtnis, geeignete Tools (mit dem sie ihre Aussenwelt verändern können) und weitere kognitive Fähigkeiten verfügen.

![image](agent.png)
