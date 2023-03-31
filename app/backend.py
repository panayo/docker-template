from flask import Flask, jsonify, request
# import joblib
# from helper import prepare_text
# from transformers import BertForSequenceClassification, BertTokenizerFast
# import transformers
# import sys


app = Flask(__name__)

#  #--------------------------------Load the models--------------------------------#
# sentiment_path_model = './models/sentiment_model/bert-base-sentiment_model'
# sentiment_model = BertForSequenceClassification.from_pretrained(sentiment_path_model)
# tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
# sentiment_text_classification = transformers.pipeline('sentiment-analysis', model=sentiment_model, tokenizer=tokenizer)


# emotion_path_model = './models/emotion_model/bert-base-emotion_model'
# emotion_model = BertForSequenceClassification.from_pretrained(emotion_path_model)
# tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
# emotion_text_classification = transformers.pipeline('text-classification', model=emotion_model, tokenizer=tokenizer)

# #---------------------------------------------------------------------------------#


@app.route('/predict', methods=['POST'])

def predict():
    data = request.get_json()
    text = data['text']
    # preprocessed_text = prepare_text(data['text'])
    # predicted_sentiment = sentiment_text_classification.predict(preprocessed_text)
    # predicted_emotion = emotion_text_classification.predict(preprocessed_text)

    response = {
        "text": data['text']}

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6000,debug=True)
