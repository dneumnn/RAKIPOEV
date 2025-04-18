# Referenzarchitektur KI-Plattform für die Öffentliche Verwaltung

Dieses Repo beinhaltet ein Exposee für die Referenzarchitektur **KI-Plattform für die Öffentliche Verwaltung**

RAKIPOEV ist der Arbeitsname für das Exposee.

Im Anschluss an das Exposee soll eine Referenzimplementierung erstellt werden.

Oberstes Ziel für die Referenzimplementierung ist eine den Anforderungen der öffentlichen Verwaltung genügende Implementierung unter Verwendung von Open-Source Komponenten.

Die Dokumentation wird mittels MkDocs erstellt. [MkDocs](https://www.mkdocs.org) generiert auf Basis von Markup Dateien eine Dokumentation als Web-Anwendung. Diese kann dann als GitHub oder GitLab Pages deployed werden.

## Dokumentation mit MkDocs

Die Dokumentation erfolgt im Verzeichnis RAKIPOEV-docs. RAKIPOEV-docs ist das root-Verzeichnis der Dokumentation.

- [MkDocs](https://www.mkdocs.org) 
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) documentation framework auf Basis von MkDocs

### Installation MkDocs

```bash
conda create --name "mkdocs" python=3.11
conda activate mkdocs
pip install mkdocs
pip install mkdocs-material
pip install mkdocs-drawio
pip install mkdocs-mermaid2-plugin
```

Für das draw.io-PlugIn müssen die Microsoft Build Tools für C++ installiert sein.
(https://visualstudio.microsoft.com/de/visual-cpp-build-tools/)

Erstelle einen neue leere Dokumentation. Nicht notwendig, da im Repository bereits vorhanden.

```bash
cd RAKIPOEV-docs
mkdocs new .
```

### Start Webserver

Start der Dokumentations-Webseite auf <http://127.0.0.1:8000/>:

```bash
cd RAKIPOEV-docs
mkdocs serve
```

Eine vollständige Dokumentation findet sich unter [mkdocs](https://www.mkdocs.org) und [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

### Project layout

Dokumentation findet innerhalb docs statt.

```code
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
```

### Publizierung

Publish the website on [GitHub or GitLab Pages](https://squidfunk.github.io/mkdocs-material/publishing-your-site/).

```bash
cd RAKIPOEV-docs 
mkdocs gh-deploy
```

Delete old files before redeploying your page with:

```bash
cd RAKIPOEV-docs 
mkdocs gh-deploy --clean --dirty --force
```
