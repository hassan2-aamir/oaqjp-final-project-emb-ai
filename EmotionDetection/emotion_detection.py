'''URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }'''
import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    status_code = response.status_code
    if status_code == 400:
        return {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None,"dominant_emotion":None}
    if status_code != 200:
        return {"error":response["statusMessage"]}
    response = response.json()
    max_emotion = max(response["emotionPredictions"][0]["emotion"], key=response["emotionPredictions"][0]["emotion"].get)
    dominant_emotion = max_emotion.capitalize()
    return {"anger":response["emotionPredictions"][0]["emotion"]["anger"], "disgust":response["emotionPredictions"][0]["emotion"]["disgust"], "fear":response["emotionPredictions"][0]["emotion"]["fear"], "joy":response["emotionPredictions"][0]["emotion"]["joy"], "sadness":response["emotionPredictions"][0]["emotion"]["sadness"],"dominant_emotion":dominant_emotion}
    

    
