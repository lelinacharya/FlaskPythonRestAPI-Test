import markdown
import os
import shelve

# Import the framework
from flask import Flask , g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create Api
api = Api(app)

def get_db():
    db = getattr(g,'_databse', None)
    if db is None:
        db = g._databse = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(Exception):
    db = getattr(g,'_databse', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    # Open the README.md file
    with open(os.path.dirname(app.root_path) + './README.md', 'r') as markdown_file:
        
        #Read the file
        content = markdown_file.read()
        
        # Convert to HTML
        return markdown.markdown(content)
    
class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        
        devices = []
        
        for key in keys:
            devices.append(shelf[key])
            
        return {'message':'Success Shelf DB', 'data': devices}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)
        
        # Pass the arg into an object
        args = parser.parse_args()
        
        shelf = get_db()
        shelf[args['identifier']] = args
        
        return {'message':'Device Registered', 'data': args}, 201
    
class Device(Resource):
    def get(self, identifier):
        shelf = get_db()
        
        # If device doesn't exist return error
        if not (identifier in shelf):
            return {'message':'Device not found', 'data': {}}, 404
                    
        return {'message':'Device found', 'data': shelf[identifier]}, 200
    
    def delete(self, identifier):
        shelf = get_db()
        
        # If device doesn't exist return error
        if not (identifier in shelf):
            return {'message':'Device not found', 'data': {}}, 404
                    
        del shelf[identifier]
        return '',204
        
    
api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/devices/<string:identifier>')