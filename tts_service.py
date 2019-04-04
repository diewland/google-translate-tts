from flask import Flask, Response, request, render_template
from flask_cors import CORS
from translate_tts import TranslateTTS

app = Flask(__name__)
tts = TranslateTTS()
CORS(app)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/tts", methods=['GET'])
def service_tts():
    msg = request.args.get('msg')
    lang = request.args.get('lang')

    # msg not found
    if msg is None:
        return render_template('index.html')

    # lang not found
    if lang is None:
        lang = 'th-TH'

    # return mp3 content
    return Response(tts.speak(msg, lang), mimetype='audio/mp3')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
