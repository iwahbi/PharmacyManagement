from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/IhssaneWahbiM'  
mongo = PyMongo(app)

# Route for adding a new drug
@app.route('/drugs', methods=['POST'])
def add_drug():
    try:
        data = request.json
        drugs_collection = mongo.db.drugs
        result = drugs_collection.insert_one(data)
        return jsonify({'message': 'Drug added successfully', 'id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route for getting all drugs
@app.route('/drugs', methods=['GET'])
def get_all_drugs():
    try:
        drugs_collection = mongo.db.drugs
        drugs = list(drugs_collection.find())
        return jsonify({'drugs': drugs})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route for getting a specific drug by ID
@app.route('/drugs/<drug_id>', methods=['GET'])
def get_drug(drug_id):
    try:
        drugs_collection = mongo.db.drugs
        drug = drugs_collection.find_one({'_id': ObjectId(drug_id)})
        if drug:
            return jsonify({'drug': drug})
        else:
            return jsonify({'message': 'Drug not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route for updating a drug by ID
@app.route('/drugs/<drug_id>', methods=['PUT'])
def update_drug(drug_id):
    try:
        data = request.json
        drugs_collection = mongo.db.drugs
        result = drugs_collection.update_one({'_id': ObjectId(drug_id)}, {'$set': data})
        if result.modified_count > 0:
            return jsonify({'message': 'Drug updated successfully'})
        else:
            return jsonify({'message': 'Drug not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route for deleting a drug by ID
@app.route('/drugs/<drug_id>', methods=['DELETE'])
def delete_drug(drug_id):
    try:
        drugs_collection = mongo.db.drugs
        result = drugs_collection.delete_one({'_id': ObjectId(drug_id)})
        if result.deleted_count > 0:
            return jsonify({'message': 'Drug deleted successfully'})
        else:
            return jsonify({'message': 'Drug not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
