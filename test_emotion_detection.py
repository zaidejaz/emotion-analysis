from EmotionDetection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detection.emotion_detector("I am glad this happened")["dominant_emotion"], 'joy')
        self.assertEqual(emotion_detection.emotion_detector("I am really mad about this	")["dominant_emotion"], 'anger')
        self.assertEqual(emotion_detection.emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], 'disgust')
        self.assertEqual(emotion_detection.emotion_detector("I am so sad about this")["dominant_emotion"], 'sadness')
        self.assertEqual(emotion_detection.emotion_detector("I am really afraid that this will happen")["dominant_emotion"], 'fear')

unittest.main()