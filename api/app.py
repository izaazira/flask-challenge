from programming_challenge import ProgrammingChallenge
import json
from config import *

programmingChallenge = ProgrammingChallenge()

@app.route('/')
def index():
    res = {'messages' : 'Welcome to Programming Challenge','code':200}
    return jsonify(res)
 
@app.route('/api')
def api_index():
    res = {'messages' : 'Welcome to Programming Challenge API','code':200}
    return jsonify(res)

@app.route('/api/generate-report', methods=['POST'])
def api_generate_report():
    request_data = request.json
    return jsonify(programmingChallenge.generate_report(request_data.get('file')))


@app.route('/api/get-data')
def api_get_data():
    return jsonify(programmingChallenge.generate_random_data())

@app.route('/api/download/', methods=['GET'])
def api_download_file():
    if request.args.get('file'):
        return programmingChallenge.download_report(request.args.get('file'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
