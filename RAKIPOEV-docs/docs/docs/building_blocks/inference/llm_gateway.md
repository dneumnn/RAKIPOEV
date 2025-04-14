# LLM-Gateway

Das LLM-Gateway liefert eine einheitliche Schnittstelle zu LLMs. Es unterstützt das [OpenAI API](https://platform.openai.com/docs/overview) und erfüllt folgende Aufgaben innerhalb der Plattform.

## Anforderungen

- zu Verfügungstellung der OpenAI API /v1/chat/completions und /v1/embedding für Chat und Vector-Embeddings
- Routing der Anfragen auf verschiedene On-Premise Inference Backends (Inference Engines) oder öffentliche Modell Anbieter
- Load Balancing
- Verwaltung von Berechtigungen auf Organisation, Team und Benutzer-Ebene für die Nutzung von Modellen
- Autorisierung (darf das Modell vom anfragenden Client genutzt werden?)
- Tracking des Token-Verbrauchs bzw. der Kosten: sowohl der Input- als auch der Output-Tokens
- Überprüfen von Rate Limits (request per minute, tokens per minute)
- Callbacks (Anbindung von LLM-Engineering Plattformen, wie z.B. Langfuse)
- Logging: Anbindung von Log-Providern
- Post-Processing (zur Integration von z.B. Guardrails)
- Streaming und Unterstützung für asynchrone Anfragen
- Fehler-Management mittels Fallbacks: Automatischer Retry, ...

## Architektur

![image](llm_gateway.png)


## Kandidaten für eine Implementierung

**[LiteLLM.proxy](https://docs.litellm.ai/docs/simple_proxy)**

| Anforderung | Grad der Füllung |
| --- | ----------- |
| Open Source | [MIT](https://github.com/BerriAI/litellm?tab=License-1-ov-file#readme) mit Ausnahme der [Enterprise Features](https://docs.litellm.ai/docs/proxy/enterprise) |
| SSL-Fähigkeit | SSL Terminierung muss über einen vorgeschalteten Server erfolgen (z.B. Nginx, Apache, etc.) |
| User Verwaltung | Organisation - Team - User |
| Mandantenfähigkeit | User Verwaltung kennt Organisation und Team. Über Organisation lässt sich eventuell eine Mandantenfähigkeit herstellen |
| Spent Management | ja |
| Token Usage Tracking | ja |
| Rate Lmit | rpm und tpm |
| Authentifizierung via IDP | Eventuell via [Event Hook for SSO Login](https://docs.litellm.ai/docs/proxy/custom_sso)|
| Callbacks | ja |
| Guardrails | BETA |
| Erweiterbarkeit durch Plugins | [Custom Plugins](https://docs.litellm.ai/docs/proxy/call_hooks) |


Swagger Documentation: <https://litellm-api.up.railway.app>
