#import unittest library
import unittest

# Import the function to be tested
from EmotionDetection.emotion_detection import emotion_detector

# Create a class that inherits from unittest.TestCase
class TestEmotionDetection(unittest.TestCase):
    # Define a test method
    def test_joy(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "Joy")
    def test_sadness(self):
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "Sadness")
    def test_anger(self):
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "Anger")
    def test_fear(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "Fear")
    def test_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "Disgust")


