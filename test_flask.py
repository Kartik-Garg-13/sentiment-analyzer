from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "hello, Flask is working!"
@app.route('/about')
def about():
    return "this is the sentiment analyzer project"
@app.route('/echo', methods=['POST'])
def echo():
    data=request.get_json()
    name=data['name']
    return jsonify({'message':'hello '+name})
if __name__ == '__main__':
    app.run(debug=True)