<div align="center">
[🇬🇧 English](README.md) | **Deutsch** | [🇮🇷 فارسی](README.fa.md)
</div>

---

# 🤖 KI-Chatbot für Telegram

> **Erstelle deinen eigenen KI-gestützten Telegram-Chatbot – entweder mit einer externen KI-API oder einem lokalen LLM mit Ollama.**

Ein einfaches und einsteigerfreundliches Python-Projekt, das **Telegram** mit einem KI-Modell verbindet.

Dieses Repository bietet **zwei Möglichkeiten**, einen KI-Chatbot zu betreiben:

* ☁️ **API-Modus** – verbindet Telegram mit einer externen KI-API, beispielsweise einer OpenAI-kompatiblen API.
* 🖥️ **Lokaler Modus** – führt ein KI-Modell lokal mit **Ollama** aus, ohne deine Unterhaltungen an eine externe KI-API senden zu müssen.

Das Projekt wurde so entwickelt, dass es leicht verständlich, anpassbar und erweiterbar ist.

---

## ✨ Funktionen

* 🤖 KI-gestützte Unterhaltungen direkt in Telegram
* 💬 Einfacher textbasierter Chat
* ⚡ Asynchrone Verarbeitung von Telegram-Nachrichten
* ☁️ Unterstützung für externe KI-APIs
* 🖥️ Unterstützung für lokale KI-Modelle mit Ollama
* 🔐 Konfiguration von API-Schlüsseln und Telegram-Bot-Token
* 🧩 Einfach anzupassender Python-Code
* ⏳ Status-/Verarbeitungsmeldungen während der Antwortgenerierung
* 🛠️ Einsteigerfreundliche Implementierung

---

# 🏗️ So funktioniert das Projekt

Der Ablauf ist bewusst einfach gehalten:

```text
                 Telegram
                    │
                    ▼
             ┌──────────────┐
             │ Telegram-Bot │
             └───────┬──────┘
                     │
              Benutzer sendet
                eine Nachricht
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   ☁️ API-MODUS            🖥️ LOKALER MODUS
          │                     │
          ▼                     ▼
   Externe KI-API             Ollama
          │                     │
          └──────────┬──────────┘
                     ▼
             KI-generierte Antwort
                     │
                     ▼
                 Telegram
```

---

# 📁 Projektstruktur

```text
Ai-chatbot-in-telegram/
│
├── chatbot(api).py       # ☁️ KI-Chatbot über API
├── chatbot(local).py     # 🖥️ Lokaler Ollama-Chatbot
├── .gitignore
└── README.md
```

Das Repository hält die Implementierung bewusst kompakt, damit du leicht verstehen kannst, wie Telegram und KI-Modelle miteinander kommunizieren.

---

# ☁️ Option 1 – API-basierter Chatbot

Die API-Version verwendet:

* Python
* `python-telegram-bot`
* `httpx`
* Eine OpenAI-kompatible KI-API

Die Implementierung sendet die Nachricht des Benutzers an einen konfigurierten API-Endpunkt und verarbeitet anschließend die Antwort des KI-Modells.

## Architektur

```text
Telegram
   │
   ▼
Python Telegram Bot
   │
   ▼
HTTP-Anfrage
   │
   ▼
KI-API
   │
   ▼
KI-Antwort
   │
   ▼
Telegram
```

---

## 1. Abhängigkeiten installieren

```bash
pip install python-telegram-bot httpx
```

---

## 2. Bot konfigurieren

Öffne:

```text
chatbot(api).py
```

Konfiguriere die benötigten Werte:

```python
API_URL = "DEINE_API_URL"
API_KEY = "DEIN_API_KEY"
BOT_TOKEN = "DEIN_TELEGRAM_BOT_TOKEN"
MODEL_NAME = "DEIN_MODELLNAME"
```

> ⚠️ **Wichtig:** Veröffentliche niemals echte API-Schlüssel oder Telegram-Bot-Tokens auf GitHub.

---

## 3. Bot starten

Da der Dateiname Klammern enthält, sollte die Datei so gestartet werden:

```bash
python "chatbot(api).py"
```

Wenn alles korrekt eingerichtet ist, sollte der Bot eine entsprechende Startmeldung ausgeben.

Danach kannst du deinen Telegram-Bot öffnen und ihm eine Nachricht senden.

---

# 🖥️ Option 2 – Lokale KI mit Ollama

Du möchtest die KI **vollständig lokal** ausführen?

Dieses Repository enthält auch eine Ollama-Implementierung.

Bei dieser Variante läuft das KI-Modell auf deinem eigenen Computer, anstatt deine Anfragen an eine externe KI-API zu senden.

## Architektur

```text
Telegram
   │
   ▼
Python Telegram Bot
   │
   ▼
Ollama
   │
   ▼
Lokales KI-Modell
   │
   ▼
KI-Antwort
   │
   ▼
Telegram
```

---

## 1. Ollama installieren

Installiere Ollama für dein Betriebssystem.

Anschließend kannst du überprüfen, ob die Installation funktioniert:

```bash
ollama --version
```

Installierte Modelle anzeigen:

```bash
ollama list
```

---

## 2. Ein KI-Modell herunterladen

Zum Beispiel:

```bash
ollama pull llama3.2
```

Du kannst selbstverständlich auch ein anderes von Ollama unterstütztes Modell verwenden.

---

## 3. Python-Abhängigkeiten installieren

```bash
pip install python-telegram-bot ollama
```

---

## 4. Modell konfigurieren

Öffne:

```text
chatbot(local).py
```

Suche nach:

```python
model='youre_local_Ai_name'
```

und ersetze es beispielsweise durch:

```python
model='llama3.2'
```

Außerdem musst du:

```python
"YOUR_BOT_TOKEN"
```

durch deinen echten Telegram-Bot-Token ersetzen.

---

## 5. Bot starten

```bash
python "chatbot(local).py"
```

Öffne anschließend Telegram und beginne mit deinem lokalen KI-Modell zu chatten.

---

# 🤖 Einen Telegram-Bot erstellen

Für beide Varianten benötigst du einen Telegram-Bot-Token.

## Schritt 1 – BotFather öffnen

Suche in Telegram nach:

```text
@BotFather
```

---

## Schritt 2 – Einen Bot erstellen

Sende:

```text
/newbot
```

Folge anschließend den Anweisungen von Telegram.

Du benötigst:

* Einen Anzeigenamen
* Einen eindeutigen Benutzernamen, der mit `bot` endet

BotFather stellt dir anschließend einen Token zur Verfügung, der ungefähr so aussieht:

```text
123456789:ABCxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Schritt 3 – Token konfigurieren

Trage den Token in die entsprechende Python-Datei ein.

> 🔐 **Sicherheit:** Veröffentliche deinen Bot-Token niemals öffentlich.

Falls dein Token versehentlich veröffentlicht wurde, solltest du ihn über BotFather widerrufen und einen neuen erstellen.

---

# 💬 Den Bot verwenden

Sobald dein Bot läuft:

## Bot starten

Sende in Telegram:

```text
/start
```

Der Bot bestätigt, dass er bereit ist.

## Eine Nachricht senden

Zum Beispiel:

```text
Erkläre mir Python Decorators einfach.
```

Der Bot verarbeitet die Anfrage und sendet anschließend die KI-generierte Antwort zurück.

Beispiel:

```text
Du:
Erkläre mir Python Decorators einfach.

Bot:
Ein Decorator ist eine Funktion, die das Verhalten
einer anderen Funktion erweitert oder verändert...
```

---

# ⚙️ Anpassungsmöglichkeiten

Das Projekt ist bewusst einfach gehalten und kann problemlos erweitert werden.

## 🧠 KI-Modell

Du kannst das verwendete Modell sowohl im API-Modus als auch im Ollama-Modus ändern.

---

## 🌡️ Temperatur

Die API-Implementierung verwendet aktuell:

```python
"temperature": 0.7
```

Die lokale Implementierung verwendet:

```python
'temperature': 0.1
```

Eine höhere Temperatur kann zu abwechslungsreicheren Antworten führen.

Eine niedrigere Temperatur führt normalerweise zu deterministischeren Antworten.

---

## 📏 Maximale Antwortlänge

Die API-Version verwendet:

```python
"max_tokens": 512
```

Die Ollama-Version verwendet:

```python
'num_predict': 512
```

Diese Werte können je nach Modell und Anwendungsfall angepasst werden.

---

# 🔐 Sicherheit

**Speichere niemals geheime Zugangsdaten direkt in einem öffentlichen Repository.**

Vermeide beispielsweise:

```python
API_KEY = "echter-geheimer-api-key"
BOT_TOKEN = "echter-telegram-token"
```

Verwende stattdessen Umgebungsvariablen.

Zum Beispiel:

```bash
export TELEGRAM_BOT_TOKEN="dein-token"
export AI_API_KEY="dein-api-key"
```

In Python:

```python
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("AI_API_KEY")
```

Du kannst auch eine `.env`-Datei verwenden.

Beispiel:

```env
TELEGRAM_BOT_TOKEN=dein_telegram_token
AI_API_KEY=dein_api_key
```

Stelle sicher, dass `.env` in deiner `.gitignore` enthalten ist:

```gitignore
.env
__pycache__/
*.pyc
```

---

# 🛠️ Fehlerbehebung

## Der Bot startet nicht

Überprüfe zuerst deinen Telegram-Bot-Token.

```text
YOUR_BOT_TOKEN
```

muss durch deinen echten Token ersetzt werden.

---

## Der API-Modus gibt einen Fehler zurück

Überprüfe:

* API-URL
* API-Key
* Modellname
* Internetverbindung
* Kompatibilität der API
* Format der API-Antwort

---

## Der Ollama-Modus funktioniert nicht

Überprüfe zunächst Ollama:

```bash
ollama list
```

Stelle anschließend sicher, dass das in `chatbot(local).py` konfigurierte Modell tatsächlich installiert ist.

Zum Beispiel:

```python
model='llama3.2'
```

Falls das Modell noch nicht installiert ist:

```bash
ollama pull llama3.2
```

---

## Der Bot antwortet langsam

Bei lokalen KI-Modellen hängt die Geschwindigkeit unter anderem von folgenden Faktoren ab:

* CPU
* GPU
* RAM
* Größe des KI-Modells
* Ollama-Konfiguration

Im API-Modus hängt die Geschwindigkeit hauptsächlich von deiner Internetverbindung und dem verwendeten KI-Anbieter bzw. Modell ab.

---

# 🚀 Ideen für zukünftige Verbesserungen

Dieses Projekt bietet eine einfache Grundlage für weitere Entwicklungen.

Mögliche Erweiterungen:

* 🧠 Gesprächsspeicher
* 👤 Individueller Chatverlauf für jeden Benutzer
* 🔄 `/reset`-Befehl
* 🎙️ Unterstützung für Sprachnachrichten
* 🖼️ Bildverständnis
* 🎨 KI-Bildgenerierung
* 📎 Verarbeitung von Dateien und Dokumenten
* 🌍 Mehrsprachige Unterstützung
* 👥 Unterstützung für Telegram-Gruppen
* 🔐 Benutzerautorisierung
* ⚙️ Konfiguration über Umgebungsvariablen
* 📝 Verbesserte Protokollierung
* 🐳 Docker-Unterstützung
* ☁️ Deployment auf VPS oder Cloud-Server
* 🔌 Unterstützung für mehrere KI-Anbieter
* 📊 Token- und Nutzungsstatistiken

---

# 🧪 Entwicklung

Repository klonen:

```bash
git clone https://github.com/kasranaqhdpur/Ai-chatbot-in-telegram.git
```

In das Projektverzeichnis wechseln:

```bash
cd Ai-chatbot-in-telegram
```

Eine virtuelle Python-Umgebung erstellen:

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Abhängigkeiten installieren:

```bash
pip install python-telegram-bot httpx ollama
```

Wähle anschließend entweder den API-Modus oder den lokalen Ollama-Modus und konfiguriere die benötigten Zugangsdaten bzw. das gewünschte Modell.

---

# 🤝 Mitmachen

Beiträge und Verbesserungen sind herzlich willkommen! 🎉

Wenn du eine Idee hast, die das Projekt verbessern könnte:

### 1. Repository forken

### 2. Einen neuen Branch erstellen

```bash
git checkout -b feature/meine-neue-funktion
```

### 3. Änderungen durchführen

### 4. Änderungen committen

```bash
git commit -m "Add my new feature"
```

### 5. Branch pushen

```bash
git push origin feature/meine-neue-funktion
```

### 6. Pull Request erstellen

Fehlerberichte, Feature-Ideen, Verbesserungen der Dokumentation und Code-Beiträge sind willkommen.

---

# ⭐ Projekt unterstützen

Wenn dir dieses Projekt geholfen hat, etwas Neues zu lernen oder deinen eigenen Telegram-KI-Bot zu erstellen:

**⭐ Gib dem Repository einen Star auf GitHub!**

Das hilft dabei, das Projekt für weitere Entwickler sichtbar zu machen.

---

# 📜 Lizenz

Dieses Repository enthält derzeit keine Lizenzdatei.

Wenn du das Projekt als Open-Source-Projekt veröffentlichen und anderen die Nutzung, Änderung oder Weiterverteilung erlauben möchtest, solltest du eine passende Lizenz hinzufügen, beispielsweise die **MIT License**.

---

# 👨‍💻 Autor

Erstellt von **kasranaqhdpur**.

Repository:

https://github.com/kasranaqhdpur/Ai-chatbot-in-telegram

---

# 💡 Warum dieses Projekt?

Einen KI-Chatbot zu bauen muss nicht kompliziert sein.

Dieses Projekt zeigt die grundlegende Idee:

```text
Telegram
   +
Python
   +
KI
   =
🤖 Dein eigener Telegram-KI-Assistent
```

Egal, ob du eine Cloud-KI-API verwenden oder ein LLM vollständig lokal mit Ollama ausführen möchtest – dieses Repository bietet dir eine einfache Grundlage für dein eigenes Projekt.

**Baue es. Passe es an. Mach es zu deinem eigenen Projekt. 🚀**
