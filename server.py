"""
Emotion Detector Server module
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detection

app = Flask("Emotion Detector")

@app.route('/')
def index():
    """
    Homepage
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
    Detect emotion api
    """
    text = request.args.get("textToAnalyze")
    emotions = emotion_detection.emotion_detector(text)

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant_emotion = emotions["domainant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy' {joy}  'sadness': {sadness}."
    f" The dominant emotion is {dominant_emotion}")
