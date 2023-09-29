import requests
import base64
import json
import config

api_key = config.google_texttospeech_api_key

async def synthesize_text(text, loc, api_key=api_key):
    url = "https://texttospeech.googleapis.com/v1/text:synthesize?key={}".format(api_key)
    data = {
        "input": {"text": text},
        "voice": {"languageCode": loc, "ssmlGender": "SSML_VOICE_GENDER_UNSPECIFIED"},
        "audioConfig": {"audioEncoding": "OGG_OPUS"}
    }
    response = requests.post(url, json=data)
    response_json = json.loads(response.content)
    
    audio_base64 = response_json.get('audioContent', '')
    audio_data = base64.b64decode(audio_base64)

    return audio_data