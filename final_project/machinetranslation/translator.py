import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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

def english_to_french(englishText):
    """
    This function translate English to French
    """
    FRENCHTEXT = language_translator.translate(
    text = englishText,
    model_id = 'en-fr').get_result()
    return FRENCHTEXT

def french_to_english(frenchText):
    """
    This function translate French to English
    """
    ENGLISHTEXT = language_translator.translate(
    text = frenchText,
    model_id = 'fr-en').get_result()
    return ENGLISHTEXT