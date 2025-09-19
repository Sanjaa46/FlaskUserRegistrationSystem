from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello_api():
    return jsonify({"message": "Hello from API!"})

if __name__ == '__main__':
    app.run(debug=True)