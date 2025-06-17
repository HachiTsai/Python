"""emotion_detection.py - Watson NLP Emotion Predict API 呼叫範例"""

import requests
import json

def emotion_predict(text_to_analyse):
    """
    呼叫 Watson NLP Emotion Predict API，回傳情緒分析結果（dict）。
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=payload, headers=headers)
    # 轉成 dict
    return response.json() if response.headers.get('Content-Type','').startswith('application/json') else json.loads(response.text)

def emotion_detector(text):  # sourcery skip: extract-method
    """
    Watson NLP Emotion Predict API，回傳指定格式的情緒分數與主導情緒。
    """
    result = emotion_predict(text)
    # 預設分數
    anger = disgust = fear = joy = sadness = 0.0
    try:
        emotion_scores = result['emotionPredictions'][0]['emotion']
        anger = emotion_scores.get('anger', 0.0)
        disgust = emotion_scores.get('disgust', 0.0)
        fear = emotion_scores.get('fear', 0.0)
        joy = emotion_scores.get('joy', 0.0)
        sadness = emotion_scores.get('sadness', 0.0)
        # 找出分數最高的情緒
        emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    except (KeyError, IndexError, TypeError):
        return {'error': 'Invalid response from API', 'raw': result}

# 範例用法
if __name__ == "__main__":
    result = emotion_predict("I am so happy and excited to use Watson NLP!")
    print(result)
