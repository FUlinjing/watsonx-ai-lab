from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Hardcoded API key for demonstration purposes
API_KEY = 'ala_ma_kota'

# Decorator to check if the provided API key is valid
def api_key_required(f):
    def decorated(*args, **kwargs):
        provided_key = request.headers.get('API-Key')
        if not provided_key or provided_key != API_KEY:
            return jsonify({'message': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/resource', methods=['POST'])
@api_key_required
def create_resource():
    data = request.json
    if not data:
        return jsonify({'message': 'No data provided'}), 400 
    
    # Process the data and create a resource (for example, store in a database)
    # Your implementation logic here
    
    return jsonify({'message': 'Resource created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)

