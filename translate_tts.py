import requests

class TranslateTTS:

    TTS_API = "https://translate.google.com/translate_tts"

    def __init__(self):
        pass

    def speak(self, msg, lang_code='th-TH'):
        r = requests.get(self.TTS_API, params={
            'q'     : msg,
            'tl'    : lang_code,
            'ie'    : 'UTF-8',
            'client': 'tw-ob',
        })
        return r

    def save_mp3(self, msg, lang_code='th-TH', out_mp3='out.mp3'):
        r = self.speak(msg, lang_code)
        with open(out_mp3, 'wb') as f:
            f.write(r.content)

if __name__ == "__main__":

    msg = "ไม่หวันไหว แม้ใจจะสุดเหงา อยากให้เรามั่นคงอยู่อย่างนี้"

    tts = TranslateTTS()
    tts.save_mp3(msg)
