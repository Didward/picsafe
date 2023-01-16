from flask import Flask, request

app = Flask(__name__)


@app.route('/wordcount', methods=['GET'])
def word_count():
    text = request.args.get('text')
    if text is None:
        return "Please provide a text in the 'text' query parameter", 400
    word_count = len(text.split())
    return {"word_count": word_count}, 200


if __name__ == '__main__':
    app.run()
