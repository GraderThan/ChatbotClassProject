from flask import Flask, request, jsonify, send_from_directory
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

import torch

app = Flask(__name__, static_folder="frontend")

model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)


# Serve the HTML file directly from the static folder
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')  # type: ignore


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/api/get_response', methods=['POST'])
def get_response():

    user_input = request.json.get('message')  # type: ignore

    inputs = tokenizer([user_input], return_tensors="pt")

    # Generate BlenderBot's response
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
