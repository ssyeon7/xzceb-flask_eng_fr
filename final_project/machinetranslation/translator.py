import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Translate from english to french"""
    if english_text == "" or english_text is None:
        return "You need to send an input"

    french_tr = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    print(json.dumps(french_tr, indent=2, ensure_ascii=False))

    return french_tr["translations"][0]["translation"]

def french_to_english(french_text):
    """Translate from french to english"""
    if french_text == "" or french_text is None:
        return "You need to send an input"

    english_tr = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    print(json.dumps(english_tr, indent=2, ensure_ascii=False))

    return english_tr["translations"][0]["translation"]
