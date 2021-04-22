from flask import Flask, jsonify, request
from helpers.findIndexNumber import findIndexNumber
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def testServer():
  return jsonify({
    "ok": True,
    "message": "This server is running"
  })

@app.route('/findindex', methods=['POST'])
def getFindIndex():
  array_to_find_index_number = request.json['array']
  result = findIndexNumber(array_to_find_index_number)

  return jsonify({
    "ok": True,
    "message": "This is the index found",
    "data": result
  })

if __name__ == '__main__':
  app.run()