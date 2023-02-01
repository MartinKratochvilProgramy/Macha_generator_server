from flask import Flask, jsonify, request
from flask_cors import CORS
import tensorflow as tf
from model.OneStep import OneStep 
from model.Model import Model
from model.Dataset import Dataset

app = Flask(__name__)
CORS(app)

@app.route('/get_text', methods = ['POST'])
def hello():
    try:
        data = request.get_json()

        input_string = data["input-string"]
        length = int(data["length"])

        text = one_step_model.generate(input_string, length)

        return jsonify(message = text)
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    dataset = Dataset()
    model = Model(
        vocab_size=dataset.get_vocab_length(),
        embedding_dim=256,
        rnn_units=512
        )
    model.load_weights(tf.train.latest_checkpoint('./model/training_checkpoints'))
    one_step_model = OneStep(
        model = model, 
        chars_from_ids = dataset.chars_from_ids, 
        ids_from_chars = dataset.ids_from_chars,
        temperature = 0.001
    )
    app.run(debug=True, host="localhost", port=3000)