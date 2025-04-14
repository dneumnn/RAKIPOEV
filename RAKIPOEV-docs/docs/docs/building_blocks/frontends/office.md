# Office-Plugins

Die Entwicklung von Office-Plugins unterscheidet sich je nach verwendetem Produkt und ggf. auch bzgl. der eingesetzten Produktversion.

## Microsoft Office 2016/2019/2024
Bei diesen Office-Version wird unter Verwendung der Visual Studio Tools for Office (VSTO) ein VSTO-Add-in auf Basis des .Net-Fameworks erstellt. Für das zugehörige GUI wird WPF (Windows Presentation Foundation) eingesetzt, dass ein responsives Design unterstützt.

## Office 365
Im Gegensatz zu früheren Office-Integration sind Plugins für Office 365 grundsätzlich Web-Addins, die auf HTML, CSS und JavaScript basieren. Die Konfiguration und Integration in das Office User Interface erfolgt über die Manifest-Datei. Der Plugin-Code wird innerhalb einer Sandbox als Browser- bzw. WebView-Control ausgeführt.


## LibreOffice / Collabora Online
Plugins werde in LibreOffice als Extensions entwickelt. Sie basieren vorzugsweise auf sogenannten UNO-Komponenten (Universal Network Objects), die innerhalb von LibreOffice mittels der durch UNO bereitgestellten Kommunikationsmechanismen verwendet werden können.

## OnlyOffice Desktop Editor / Document Server
Plugins für OnlyOffice werden sowohl für den Desktop Editor als auch für den Web Editor in Javascript erstellt. Das Plugin besteht aus mindestens einer Konfigurationsdatei (config.json), die alle Daten zur Registrierung des Plugins in OnlyOffice enthält, einer HTML-Datei (index.html) mit dem Aufrufbefehl für den Plugin-Code sowie dem Plugin-Programm (pluginCode.js). Das Plugin besitzt seinen eigenen iframe, in dem das Plugin wirken kann.
