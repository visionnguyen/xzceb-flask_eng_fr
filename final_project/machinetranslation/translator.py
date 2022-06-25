"""
    Translate module
"""
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#print(apikey + '\r\n' + url)

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

languages = language_translator.list_identifiable_languages().get_result()
#print(json.dumps(languages, indent=2))

def english_to_french(english_text):
    """
        Translate English to French function
    """
    if english_text == "":
        return "Null input"

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
        Translate French to English function
    """
    if french_text == "":
        return "Null input"

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
