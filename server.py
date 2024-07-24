from flask import Flask, request, render_template

app = Flask(__name__)

from EmotionDetection.emotion_detection import emotion_detector

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    data = request.args.get('textToAnalyze')
    response = emotion_detector(data)
    return (f"For the given statement, the system response is 'anger' : {response['anger']}, 'disgust' : {response['disgust']}, 'fear' : {response['fear']}, 'joy' : {response['joy']}, 'sadness' : {response['sadness']}, The dominant emotion is {response['dominant_emotion']}")

if __name__ == '__main__':
    app.run(debug=True)

