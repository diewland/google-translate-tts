# Google Translate TTS API
Based on this API

```
https://translate.google.com/translate_tts?ie=UTF-8&q=สวัสดีครับ&tl=th-TH&client=tw-ob
```

### Installation

```
python -m venv venv
venv\Script\activate.bat
python tts_service.py
```

### Examples

```
# web demo
http://localhost:5000/

# return mp3
http://localhost:5000/tts?msg=สวัสดีครับ
http://localhost:5000/tts?msg=helloworld&lang=en-US
```

[ WARNING ] This is not offical API. Use at your own risk.
