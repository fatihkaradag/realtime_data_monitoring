from flask import Flask

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create():
    # Logic for creating data
    return 'Create Operation'

@app.route('/read', methods=['GET'])
def read():
    # Logic for reading data
    return 'Read Operation'

@app.route('/update', methods=['PUT'])
def update():
    # Logic for updating data
    return 'Update Operation'

@app.route('/delete', methods=['DELETE'])
def delete():
    # Logic for deleting data
    return 'Delete Operation'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
