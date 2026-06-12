from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API del Festival DevOps Music Fest funcionando correctamente"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)