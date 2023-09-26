''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion and emotion score.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['joy']
    dominant_emotion = response['dominant_emotion']
    return "For the given statement, the system response is\n" \
    "'anger': {}, 'disgust':{},\n" \
    "'fear':{}, 'joy':{joy_score} and 'sadness':{}.\n" \
    "The dominant emotion is {}".format(anger_score,disgust_score,fear_score,joy_score,sadness_score,dominant_emotion)

@app.route("/")
def render_index_page():
    """
    This function render the main application page of the flask app
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
