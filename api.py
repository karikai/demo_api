import json
import flask
from flask import request, jsonify
from crud import createCRUD, deleteCRUD, readCRUD, updateCRUD

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Example CREATE HTTP Request
#{
#	"collectionName": "test",
#	"data": {
#		"author": "Kari",
#       "date": "3:24 PM"
#	}
#}
@app.route('/create', methods=['POST'])
def create():
    # Validate
    data = request.json['data']
    collectionName = request.json['collectionName']
    print(data)
    print(collectionName)

    success = createCRUD(collectionName, data)
    msg = ''

    if success:
        msg = 'Did Succeed'
    else:
        msg = "Failed"

    # Perform Operations
    return msg

#Example READ HTTP Request
#{
#	"collectionName": "test",
#	"query": {
#		"author": "Kari"
#	}
#}
@app.route('/read', methods=['POST'])
def read():
    # Validate
    query = request.json['query']
    collectionName = request.json['collectionName']
    print(query)
    print(collectionName)

    results = readCRUD(collectionName, query)
    msg = ''

    if type(results) != bool:
        msg = json.dumps(results)
    else:
        msg = "Failed"

    # Perform Operations
    return msg

#Example UPDATE HTTP Request
#{
#	"collectionName": "test",
#	"query": {
#		"author": "Kari"
#	},
#  	"data": {
#		"author": "Kari Kai"
#	}
#}
@app.route('/update', methods=['POST'])
def update():
    data = request.json['data']
    query = request.json['query']
    collectionName = request.json['collectionName']
    print(data)
    print(query)
    print(collectionName)

    success = updateCRUD(collectionName, query, data)
    msg = ''

    if success:
        msg = 'Did Succeed'
    else:
        msg = "Failed"

    # Perform Operations
    return msg

@app.route('/delete', methods=['POST'])
def delete():
    # Validate
    query = request.json['query']
    collectionName = request.json['collectionName']
    print(query)
    print(collectionName)

    success = deleteCRUD(collectionName, query)
    msg = ''

    if success:
        msg = "Did succeed"
    else:
        msg = "Failed"

    # Perform Operations
    return msg

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
