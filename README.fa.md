<div align="center">



[🇬🇧 English](README.md) | [🇩🇪 Deutsch](README.de.md) | **🇮🇷 فارسی**

</div>

---
# 🤖 ربات هوش مصنوعی تلگرام
## ✨ معرفی پروژه
*ربات هوش مصنوعی خودت را برای تلگرام بساز — با استفاده از API خارجی یا اجرای یک مدل زبانی محلی با Ollama.**

این پروژه یک ربات هوش مصنوعی ساده و کاربردی است که با **Python** ساخته شده و امکان اتصال **Telegram** به یک مدل هوش مصنوعی را فراهم می‌کند.

در این Repository دو روش مختلف برای اجرای ربات وجود دارد:

* ☁️ **حالت API** — اتصال تلگرام به یک API هوش مصنوعی خارجی
* 🖥️ **حالت محلی** — اجرای یک مدل هوش مصنوعی به‌صورت کاملاً محلی با **Ollama**

هدف پروژه این است که یک پایه ساده، قابل فهم و قابل توسعه برای ساخت ربات‌های هوش مصنوعی در تلگرام فراهم کند.

---

# ✨ امکانات

* 🤖 گفت‌وگو با هوش مصنوعی مستقیماً در Telegram
* 💬 پشتیبانی از پیام‌های متنی
* ⚡ پردازش غیرهمزمان پیام‌های Telegram
* ☁️ پشتیبانی از APIهای هوش مصنوعی خارجی
* 🖥️ پشتیبانی از مدل‌های هوش مصنوعی محلی با Ollama
* 🔐 امکان تنظیم API Key و Telegram Bot Token
* 🧩 کد ساده و قابل شخصی‌سازی
* ⏳ نمایش وضعیت هنگام پردازش درخواست
* 🛠️ مناسب برای یادگیری و توسعه پروژه‌های بزرگ‌تر

---

# 🏗️ نحوه کار پروژه

روند کلی پروژه بسیار ساده است:

```text
                 Telegram
                    │
                    ▼
             ┌──────────────┐
             │  ربات تلگرام │
             └───────┬──────┘
                     │
               پیام کاربر
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       ☁️ حالت API          🖥️ حالت محلی
          │                     │
          ▼                     ▼
       API هوش مصنوعی          Ollama
          │                     │
          └──────────┬──────────┘
                     ▼
              پاسخ هوش مصنوعی
                     │
                     ▼
                  Telegram
```

---

# 📁 ساختار پروژه

```text
Ai-chatbot-in-telegram/
│
├── chatbot(api).py       # ☁️ ربات با استفاده از API
├── chatbot(local).py     # 🖥️ ربات محلی با Ollama
├── .gitignore
├── README.md             # 🇬🇧 English
├── README.de.md          # 🇩🇪 Deutsch
└── README.fa.md          # 🇮🇷 فارسی
```

---

# ☁️ حالت اول — ربات مبتنی بر API

در این حالت، ربات تلگرام پیام کاربر را دریافت کرده و آن را به یک API هوش مصنوعی ارسال می‌کند.

### تکنولوژی‌های استفاده‌شده

* Python
* `python-telegram-bot`
* `httpx`
* یک API سازگار با OpenAI

### معماری

```text
Telegram
   │
   ▼
Python Telegram Bot
   │
   ▼
HTTP Request
   │
   ▼
AI API
   │
   ▼
AI Response
   │
   ▼
Telegram
```

---

## 1. نصب وابستگی‌ها

```bash
pip install python-telegram-bot httpx
```

---

## 2. تنظیم ربات

فایل زیر را باز کن:

```text
chatbot(api).py
```

سپس مقادیر موردنیاز را تنظیم کن:

```python
API_URL = "YOUR_API_URL"
API_KEY = "YOUR_API_KEY"
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
MODEL_NAME = "YOUR_MODEL_NAME"
```

برای مثال:

```python
API_URL = "https://example.com/v1/chat/completions"
API_KEY = "your-api-key"
BOT_TOKEN = "your-telegram-bot-token"
MODEL_NAME = "your-model"
```

> ⚠️ **هشدار:** هیچ‌وقت API Key یا Telegram Bot Token واقعی خودت را در یک Repository عمومی قرار نده.

---

## 3. اجرای ربات

به دلیل وجود پرانتز در نام فایل، از دستور زیر استفاده کن:

```bash
python "chatbot(api).py"
```

اگر تنظیمات درست باشند، ربات اجرا خواهد شد.

سپس وارد Telegram شو و به ربات خودت پیام بده.

---

# 🖥️ حالت دوم — هوش مصنوعی محلی با Ollama

اگر می‌خواهی مدل هوش مصنوعی روی کامپیوتر خودت اجرا شود، می‌توانی از **Ollama** استفاده کنی.

در این حالت، درخواست‌ها مستقیماً به یک مدل محلی ارسال می‌شوند.

### معماری

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
Local AI Model
   │
   ▼
AI Response
   │
   ▼
Telegram
```

---

## 1. نصب Ollama

ابتدا Ollama را روی سیستم خود نصب کن.

بعد از نصب، برای بررسی آن:

```bash
ollama --version
```

برای مشاهده مدل‌های نصب‌شده:

```bash
ollama list
```

---

## 2. دریافت یک مدل

برای مثال:

```bash
ollama pull llama3.2
```

البته می‌توانی از مدل‌های دیگری که Ollama پشتیبانی می‌کند نیز استفاده کنی.

---

## 3. نصب کتابخانه‌های Python

```bash
pip install python-telegram-bot ollama
```

---

## 4. تنظیم مدل

فایل زیر را باز کن:

```text
chatbot(local).py
```

قسمت مدل را پیدا کن:

```python
model='youre_local_Ai_name'
```

و آن را به مدل نصب‌شده تغییر بده:

```python
model='llama3.2'
```

همچنین مقدار:

```python
"YOUR_BOT_TOKEN"
```

را با Telegram Bot Token خودت جایگزین کن.

---

## 5. اجرای ربات

```bash
python "chatbot(local).py"
```

حالا وارد Telegram شو و با مدل هوش مصنوعی محلی خودت صحبت کن.

---

# 🤖 ساخت ربات Telegram

برای اجرای هر دو حالت، به یک Telegram Bot Token نیاز داری.

## مرحله 1 — باز کردن BotFather

در Telegram جستجو کن:

```text
@BotFather
```

---

## مرحله 2 — ساخت ربات

دستور زیر را ارسال کن:

```text
/newbot
```

سپس مراحل نمایش داده‌شده توسط Telegram را دنبال کن.

در این مرحله باید:

* یک نام برای ربات انتخاب کنی
* یک Username منحصربه‌فرد انتخاب کنی

Username ربات معمولاً باید به `bot` ختم شود.

BotFather در پایان یک Token به تو می‌دهد، چیزی شبیه:

```text
123456789:ABCxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## مرحله 3 — قرار دادن Token

Token را در فایل مربوط به ربات قرار بده.

> 🔐 **امنیت بسیار مهم است:** Token ربات خودت را در GitHub عمومی منتشر نکن.

اگر Token به‌صورت تصادفی منتشر شد، آن را از طریق BotFather باطل کن و یک Token جدید بساز.

---

# 💬 استفاده از ربات

بعد از اجرای ربات:

## شروع ربات

در Telegram ارسال کن:

```text
/start
```

سپس ربات آماده دریافت پیام خواهد بود.

## ارسال پیام

برای مثال:

```text
Python چیست؟
```

ربات درخواست را پردازش کرده و پاسخ هوش مصنوعی را ارسال می‌کند.

مثال:

```text
شما:
Python چیست؟

ربات:
Python یک زبان برنامه‌نویسی سطح بالا و محبوب است
که برای توسعه وب، هوش مصنوعی، تحلیل داده و بسیاری
از پروژه‌های دیگر استفاده می‌شود.
```

---

# ⚙️ شخصی‌سازی

این پروژه عمداً ساده طراحی شده تا بتوانی به‌راحتی آن را تغییر و توسعه بدهی.

---

## 🧠 تغییر مدل هوش مصنوعی

می‌توانی مدل مورد استفاده را در حالت API یا Ollama تغییر بدهی.

برای Ollama:

```python
model='llama3.2'
```

می‌توانی این مقدار را با مدل دیگری که روی سیستم نصب کرده‌ای جایگزین کنی.

---

## 🌡️ تنظیم Temperature

در نسخه API مقدار فعلی:

```python
"temperature": 0.7
```

است.

در نسخه محلی:

```python
'temperature': 0.1
```

است.

به‌طور کلی:

* مقدار بالاتر → پاسخ‌های متنوع‌تر
* مقدار پایین‌تر → پاسخ‌های قابل پیش‌بینی‌تر

---

## 📏 حداکثر طول پاسخ

نسخه API از:

```python
"max_tokens": 512
```

استفاده می‌کند.

نسخه Ollama از:

```python
'num_predict': 512
```

استفاده می‌کند.

این مقادیر را می‌توانی با توجه به مدل و نیاز پروژه تغییر بدهی.

---

# 🔐 امنیت

**هیچ‌وقت اطلاعات محرمانه را مستقیماً داخل کد عمومی قرار نده.**

از چنین چیزی خودداری کن:

```python
API_KEY = "real-secret-api-key"
BOT_TOKEN = "real-telegram-token"
```

بهتر است از Environment Variables استفاده کنی.

مثال:

```bash
export TELEGRAM_BOT_TOKEN="your-token"
export AI_API_KEY="your-api-key"
```

سپس در Python:

```python
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("AI_API_KEY")
```

همچنین می‌توانی از فایل `.env` استفاده کنی:

```env
TELEGRAM_BOT_TOKEN=your_telegram_token
AI_API_KEY=your_api_key
```

و حتماً `.env` را در `.gitignore` قرار بده:

```gitignore
.env
__pycache__/
*.pyc
```

---

# 🛠️ رفع مشکلات رایج

## ربات اجرا نمی‌شود

Telegram Bot Token خودت را بررسی کن.

اطمینان حاصل کن که:

```text
YOUR_BOT_TOKEN
```

با Token واقعی ربات جایگزین شده باشد.

---

## حالت API خطا می‌دهد

موارد زیر را بررسی کن:

* API URL
* API Key
* نام مدل
* اتصال اینترنت
* سازگاری API
* ساختار پاسخ API

---

## Ollama کار نمی‌کند

ابتدا مدل‌های نصب‌شده را بررسی کن:

```bash
ollama list
```

سپس مطمئن شو مدلی که در `chatbot(local).py` نوشته‌ای واقعاً نصب شده است.

برای مثال:

```python
model='llama3.2'
```

اگر مدل نصب نشده:

```bash
ollama pull llama3.2
```

---

## ربات کند پاسخ می‌دهد

سرعت مدل‌های محلی به عوامل مختلفی بستگی دارد:

* CPU
* GPU
* RAM
* اندازه مدل
* تنظیمات Ollama

در حالت API، سرعت بیشتر به اینترنت و سرویس ارائه‌دهنده API و مدل انتخاب‌شده بستگی دارد.

---

# 🚀 ایده‌هایی برای توسعه آینده

این پروژه می‌تواند به یک Telegram AI Assistant کامل تبدیل شود.

برخی قابلیت‌های پیشنهادی:

* 🧠 حافظه مکالمات
* 👤 ذخیره تاریخچه جداگانه برای هر کاربر
* 🔄 دستور `/reset`
* 🎙️ پشتیبانی از پیام صوتی
* 🖼️ پردازش و درک تصاویر
* 🎨 تولید تصاویر با هوش مصنوعی
* 📎 پردازش فایل و اسناد
* 🌍 پشتیبانی از زبان‌های مختلف
* 👥 پشتیبانی از گروه‌های Telegram
* 🔐 سیستم احراز هویت کاربران
* ⚙️ تنظیمات از طریق Environment Variables
* 📝 سیستم Logging بهتر
* 🐳 پشتیبانی از Docker
* ☁️ امکان Deploy روی VPS یا Cloud
* 🔌 پشتیبانی از چندین سرویس هوش مصنوعی
* 📊 آمار استفاده و مصرف Token

---

# 🧪 توسعه پروژه

ابتدا Repository را Clone کن:

```bash
git clone https://github.com/kasranaqhdpur/Ai-chatbot-in-telegram.git
```

وارد پوشه پروژه شو:

```bash
cd Ai-chatbot-in-telegram
```

یک Virtual Environment بساز:

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

سپس وابستگی‌ها را نصب کن:

```bash
pip install python-telegram-bot httpx ollama
```

حالا یکی از دو حالت API یا Local را انتخاب و تنظیمات مربوطه را انجام بده.

---

# 🤝 مشارکت در پروژه

از مشارکت شما در توسعه پروژه استقبال می‌کنیم! 🎉

اگر ایده‌ای برای بهتر کردن پروژه داری:

### 1. Repository را Fork کن

### 2. یک Branch جدید بساز

```bash
git checkout -b feature/my-new-feature
```

### 3. تغییرات خودت را انجام بده

### 4. تغییرات را Commit کن

```bash
git commit -m "Add my new feature"
```

### 5. Branch را Push کن

```bash
git push origin feature/my-new-feature
```

### 6. یک Pull Request ایجاد کن

گزارش Bug، پیشنهاد قابلیت جدید، بهبود مستندات و مشارکت در کد همگی مورد استقبال هستند.

---

# ⭐ حمایت از پروژه

اگر این پروژه برای یادگیری یا ساخت ربات هوش مصنوعی تلگرام به تو کمک کرد:

**⭐ به Repository در GitHub Star بده!**

این کار به دیده‌شدن پروژه و رسیدن آن به توسعه‌دهندگان بیشتر کمک می‌کند.

---

# 📜 مجوز

این Repository در حال حاضر فایل License ندارد.

اگر قصد داری پروژه را به‌صورت Open Source منتشر کنی و به دیگران اجازه استفاده، تغییر و انتشار مجدد آن را بدهی، پیشنهاد می‌شود یک License مناسب مانند **MIT License** به پروژه اضافه کنی.

---

# 👨‍💻 سازنده

ساخته‌شده توسط **kasranaqhdpur**

Repository:

https://github.com/kasranaqhdpur/Ai-chatbot-in-telegram

---

# 💡 چرا این پروژه؟

ساخت یک ربات هوش مصنوعی لزوماً پیچیده نیست.

ایده اصلی این پروژه بسیار ساده است:

```text
Telegram
   +
Python
   +
AI
   =
🤖 دستیار هوش مصنوعی تلگرام
```

چه بخواهی از یک API ابری استفاده کنی و چه بخواهی یک LLM را کاملاً به‌صورت محلی با Ollama اجرا کنی، این پروژه می‌تواند نقطه شروع مناسبی برای ساخت دستیار هوش مصنوعی شخصی خودت باشد.

**بسازش. شخصی‌سازی‌اش کن. و تبدیلش کن به پروژه خودت. 🚀**

---

<div align="center">

### 🌍 زبان‌ها

[🇬🇧 English](README.md) • [🇩🇪 Deutsch](README.de.md) • **🇮🇷 فارسی**

</div>
