''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/emotionDetector")
def sent_dectector():
    '''receives the text from the HTML interface and 
    runs emotion detection over it using emotion_detection()
    function. The output returned shows scores for each emotion.
'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is {str(response)[1:-1]}"

@app.route("/")
def render_index_page():
    '''initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
