import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    } 

    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    dominant_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

    if dominant_score == anger_score:
        dominant_emotion = 'anger'
    elif dominant_score == disgust_score:
        dominant_emotion = 'disgust'
    elif dominant_score == fear_score:
        dominant_emotion = 'fear'
    elif dominant_score == joy_score:
        dominant_emotion = 'joy'
    elif dominant_score == sadness_score:
        dominant_emotion = 'sadness'
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }